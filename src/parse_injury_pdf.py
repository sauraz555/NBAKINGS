"""Parse an Official NBA Injury Report PDF into the pipeline's `injury_overrides_<date>.json` format.

Requires the `pdftotext` command-line tool (poppler-utils). Output shape matches what
`build_analytics.py` expects: {TEAM_ABBR: {"First Last": [status, reason], ...}}.
Only teams whose report has been submitted are written, so unsubmitted teams fall back to ESPN.
"""

import glob
import json
import os
import re
import subprocess

from src.bref_parser import TEAM_NAME_TO_STD

STATUSES = ("Out", "Questionable", "Doubtful", "Probable", "Available")
_PLAYER_RE = re.compile(
    r"(?:^|\s{2,})(?P<name>[A-Za-z][A-Za-z'.\-]+(?: [A-Za-z'.\-]+)*,(?: [A-Za-z'.\-]+,)? [A-Za-z'.\-]+(?: [A-Za-z'.\-]+)*)"
    r"\s{2,}(?P<status>" + "|".join(STATUSES) + r")\b\s*(?P<reason>.*)$"
)
# PDF uses some team names that differ from Basketball Reference's.
_EXTRA_TEAM_NAMES = {"LA Clippers": "LAC"}


def _team_lookup() -> dict[str, str]:
    names = dict(TEAM_NAME_TO_STD)
    names.update(_EXTRA_TEAM_NAMES)
    return names


def _to_first_last(name: str) -> str:
    """'Murphy III, Trey' -> 'Trey Murphy III'; 'Udeh, Jr., Ernest' -> 'Ernest Udeh Jr.'."""
    parts = [p.strip() for p in name.split(",")]
    if len(parts) == 3:
        return f"{parts[2]} {parts[0]} {parts[1]}"
    return f"{parts[1]} {parts[0]}"


def parse_injury_pdf(pdf_path: str) -> tuple[str, dict[str, dict[str, list[str]]]]:
    text = subprocess.run(
        ["pdftotext", "-layout", pdf_path, "-"], capture_output=True, text=True, check=True
    ).stdout
    stamp_match = re.search(r"Injury Report: (.+)", text)
    stamp = stamp_match.group(1).strip() if stamp_match else os.path.basename(pdf_path)

    teams = _team_lookup()
    # Longest names first so "Oklahoma City Thunder" wins over partial matches.
    team_names = sorted(teams, key=len, reverse=True)
    current_team = None
    result: dict[str, dict[str, list[str]]] = {}
    lines = text.splitlines()

    def _wrapped_fragment(idx: int) -> str:
        """Reason text that the PDF wrapped onto its own deeply indented line, or ''."""
        if 0 <= idx < len(lines):
            ln = lines[idx]
            body = ln.strip()
            indent = len(ln) - len(ln.lstrip())
            if body and indent >= 40 and not _PLAYER_RE.search(ln) and "Page " not in body:
                return body
        return ""

    for i, line in enumerate(lines):
        for tn in team_names:
            if re.search(rf"(^|\s){re.escape(tn)}(\s|$)", line):
                current_team = teams[tn]
                break
        if current_team is None or "NOT YET SUBMITTED" in line:
            continue
        m = _PLAYER_RE.search(line)
        if not m:
            continue
        reason = m.group("reason").strip()
        if not reason:
            reason = " ".join(f for f in (_wrapped_fragment(i - 1), _wrapped_fragment(i + 1)) if f)
        reason = re.sub(r"^Injury/Illness - ", "", reason)
        result.setdefault(current_team, {})[_to_first_last(m.group("name"))] = [m.group("status"), reason]
    return stamp, result


def write_overrides_from_latest_pdf(target_date: str, data_dir: str) -> str | None:
    """Parse the newest PDF for `target_date` and write `injury_overrides_<date>.json`."""
    pdfs = sorted(glob.glob(os.path.join(data_dir, "injury_reports", f"Injury-Report_{target_date}_*.pdf")))
    if not pdfs:
        return None

    def _sort_key(p: str) -> tuple:
        m = re.search(r"_(\d{2})_(\d{2})(AM|PM)\.pdf$", p)
        if not m:
            return (0, 0)
        hh = int(m.group(1)) % 12 + (12 if m.group(3) == "PM" else 0)
        return (hh, int(m.group(2)))

    latest = max(pdfs, key=_sort_key)
    stamp, overrides = parse_injury_pdf(latest)
    out_path = os.path.join(data_dir, f"injury_overrides_{target_date}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(overrides, f, indent=2)
    n = sum(len(v) for v in overrides.values())
    print(f"      Parsed official injury report ({stamp}): {n} players across {len(overrides)} teams.")
    return stamp
