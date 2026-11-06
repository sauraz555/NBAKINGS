"""Basketball Reference HTML table parser and NBA team/player normalization utilities."""

from html.parser import HTMLParser
import re
import unicodedata


class BRefTableParser(HTMLParser):
    """Zero-dependency HTML table parser targeting Basketball Reference `data-stat` cells."""

    def __init__(self, target_id: str):
        super().__init__()
        self.target_id = target_id
        self.in_table = False
        self.in_thead = False
        self.in_tbody = False
        self.in_tr = False
        self.in_cell = False
        self.curr_stat = None
        self.curr_text: list[str] = []
        self.curr_row: dict[str, str] = {}
        self.rows: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        d = dict(attrs)
        if tag == "table" and d.get("id") == self.target_id:
            self.in_table = True
        elif self.in_table:
            if tag == "thead":
                self.in_thead = True
            elif tag == "tbody":
                self.in_tbody = True
            elif tag == "tr" and self.in_tbody:
                if "thead" not in (d.get("class") or ""):
                    self.in_tr = True
                    self.curr_row = {}
            elif tag in ("td", "th") and self.in_tr:
                self.in_cell = True
                self.curr_stat = d.get("data-stat") or ""
                self.curr_text = []

    def handle_endtag(self, tag: str) -> None:
        if self.in_table:
            if tag == "table":
                self.in_table = False
            elif tag == "thead":
                self.in_thead = False
            elif tag == "tbody":
                self.in_tbody = False
            elif tag == "tr" and self.in_tr:
                self.in_tr = False
                if self.curr_row:
                    self.rows.append(self.curr_row)
            elif tag in ("td", "th") and self.in_cell:
                self.in_cell = False
                if self.curr_stat:
                    self.curr_row[self.curr_stat] = "".join(self.curr_text).strip()

    def handle_data(self, data: str) -> None:
        if self.in_cell:
            self.curr_text.append(data)


def parse_bref_table(filepath: str, table_id: str) -> list[dict[str, str]]:
    """Parse a Basketball Reference HTML table (including HTML-commented tables)."""
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        raw = f.read()
    raw = raw.replace("<!--", "").replace("-->", "")
    parser = BRefTableParser(table_id)
    parser.feed(raw)
    return parser.rows


TEAM_NAME_TO_STD: dict[str, str] = {
    "Atlanta Hawks": "ATL",
    "Boston Celtics": "BOS",
    "Brooklyn Nets": "BKN",
    "Charlotte Hornets": "CHA",
    "Chicago Bulls": "CHI",
    "Cleveland Cavaliers": "CLE",
    "Dallas Mavericks": "DAL",
    "Denver Nuggets": "DEN",
    "Detroit Pistons": "DET",
    "Golden State Warriors": "GSW",
    "Houston Rockets": "HOU",
    "Indiana Pacers": "IND",
    "Los Angeles Clippers": "LAC",
    "LA Clippers": "LAC",
    "Los Angeles Lakers": "LAL",
    "Memphis Grizzlies": "MEM",
    "Miami Heat": "MIA",
    "Milwaukee Bucks": "MIL",
    "Minnesota Timberwolves": "MIN",
    "New Orleans Pelicans": "NOP",
    "New York Knicks": "NYK",
    "Oklahoma City Thunder": "OKC",
    "Orlando Magic": "ORL",
    "Philadelphia 76ers": "PHI",
    "Phoenix Suns": "PHX",
    "Portland Trail Blazers": "POR",
    "Sacramento Kings": "SAC",
    "San Antonio Spurs": "SAS",
    "Toronto Raptors": "TOR",
    "Utah Jazz": "UTA",
    "Washington Wizards": "WAS",
}

ESPN_TO_STD: dict[str, str] = {
    "WSH": "WAS",
    "GS": "GSW",
    "NO": "NOP",
    "NY": "NYK",
    "SA": "SAS",
    "UTAH": "UTA",
}


def norm_team(abbr: str) -> str:
    """Normalize ESPN or Basketball Reference team abbreviations to standard 3-letter NBA codes."""
    return ESPN_TO_STD.get(abbr, abbr)


def norm_pname(name: str) -> str:
    """Normalize player names across diacritics, suffixes, and punctuation."""
    s = unicodedata.normalize("NFKD", name).encode("ASCII", "ignore").decode("ASCII")
    s = s.lower().replace(".", "").replace("'", "").replace("-", " ").strip()
    return re.sub(r"\s+", " ", s)
