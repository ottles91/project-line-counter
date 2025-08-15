# 📊 Line Counter

A Python command-line tool to **count total lines of code** in a directory.

---

## 🚀 Features

- Scans a directory and its subdirectories
- Supports **multiple file extensions** (e.g. `.py`, `.cs`, `.js`, `.swift`)
- Counts all files if no `--ext` argument is provided
- Optionally include hidden files and directories with `--include-hidden`
- Skips unreadable or binary files
- Provides a **breakdown of lines by file type**
- Reports the number of skipped non-text/binary files

---

## 🛠️ Requirements

- Python 3.7 or later

---

## 📦 Installation

Clone this repository:

```bash
git clone https://github.com/ottles91/project-line-counter
cd line-counter
```

## ▶️ Example Usage

Basic usage (count all text-based files in a given directory):

```bash
python3 lineCounter.py /path/to/project
```

Count lines for all Python, Swift and JavaScript files:

```bash
python3 lineCounter.py /path/to/project --ext .py .swift .js
```

Include hidden files & folders:

```bash
python3 lineCounter.py /path/to/project --include-hidden
```

See help:

```bash
python3 lineCounter.py -h
```

## Example Output

```
Counting total lines of code in ./my_project...

Total lines of code: 2500

Lines by file type:
.css: 667
.html: 2204
.js: 91
.md: 43
No Extension: 30

Skipped 10 non-text/binary files.
```

## 📜 License

MIT License. Free to use and modify.
