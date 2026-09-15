import csv
from typing import NamedTuple, Optional

class CSVDialectInfo(NamedTuple):
    delimiter: str
    quotechar: str
    has_header: bool

COMMON_DELIMITERS = [",", ";", "\t", "|"]

def sniff_csv(sample_text: str) -> CSVDialectInfo:
    """Sniff CSV delimiter and header presence from sample text."""
    if not sample_text or not sample_text.strip():
        return CSVDialectInfo(delimiter=",", quotechar='"', has_header=False)

    lines = [line for line in sample_text.splitlines() if line.strip()][:10]
    sample = "\n".join(lines)

    try:
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(sample, delimiters=COMMON_DELIMITERS)
        has_header = sniffer.has_header(sample)
        return CSVDialectInfo(
            delimiter=dialect.delimiter,
            quotechar=dialect.quotechar or '"',
            has_header=has_header,
        )
    except Exception:
        # Fallback frequency count
        scores = {d: sum(line.count(d) for line in lines) for d in COMMON_DELIMITERS}
        best_delimiter = max(scores, key=scores.get)
        if scores[best_delimiter] == 0:
            best_delimiter = ","
        return CSVDialectInfo(delimiter=best_delimiter, quotechar='"', has_header=False)
