import pytest
from py_csv_sniffer import sniff_csv

def test_sniff_semicolon_csv():
    text = "name;age;city\nAlice;25;London\nBob;30;Paris"
    info = sniff_csv(text)
    assert info.delimiter == ";"
    assert info.has_header is True

def test_sniff_tab_csv():
    text = "col1\tcol2\nval1\tval2"
    info = sniff_csv(text)
    assert info.delimiter == "\t"
