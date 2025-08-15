# 📊 Line Counter

A simple Python command-line tool to **count total lines of code** in a directory.  
Supports multiple file extensions so you can count lines across languages like Python, C#, JavaScript, etc.

---

## 🚀 Features

- Recursively scans a directory and its subdirectories
- Supports **multiple file extensions** (e.g. `.py`, `.cs`, `.js`, `.swift`)
- Skips unreadable files
- Easy to extend or customize

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

## ▶️ Usage

Basic usage (count .py and .cs files in a directory):

```bash
python lineCounter.py /path/to/project
```

Specify one or more file extensions:

```bash
python lineCounter.py /path/to/project --ext .py .swift .js
```

See help:

```bash
python main.py -h
```

## 📜 License

MIT License. Free to use and modify.
