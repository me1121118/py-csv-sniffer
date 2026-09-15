# py-csv-sniffer

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/py-csv-sniffer/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Zero-dependency CSV delimiter, quote char, and header detector in pure Python.

---

## 🚀 Features

- 🪶 **Zero Dependencies**: Pure standard library (`csv`).
- 🔍 **Delimiter Detection**: Auto-identifies commas `,`, tabs `\t`, semicolons `;`, and pipes `|`.
- 📊 **Header Detection**: Checks if the first line is a header row.

---

## 📦 Installation

```bash
pip install py-csv-sniffer
```

---

## 🛠️ Quickstart

```python
from py_csv_sniffer import sniff_csv

sample = """name;age;email
Alice;28;alice@example.com
Bob;32;bob@example.com"""

dialect = sniff_csv(sample)
print(dialect.delimiter)  # ';'
print(dialect.has_header) # True
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this CSV sniffer saved you from parsing errors, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [ko-fi.com/me1121118](https://ko-fi.com/)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
