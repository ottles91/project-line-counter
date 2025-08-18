# 📊 Line Counter

A Python command-line tool to **count total lines of code** in a directory.

---

## 🚀 Features

- Scans a directory and its subdirectories
- Supports **multiple file extensions** (e.g. `.py`, `.cs`, `.js`, `.swift`)
- Counts all files if no `--ext` argument is provided
- Optionally include hidden files and directories with `--include-hidden`
- Optionally exclude certain file extensions or directories when counting all files
- Skips unreadable or binary files
- Provides a **breakdown of lines by file type**
- Reports the number of skipped non-text/binary files

---

## 🛠️ Requirements

- Python 3.7 or later

---

## Installing Python

This project requires **Python 3.8+**.  
If you don’t already have Python installed, follow the steps below:

### Windows

1. Download the latest stable release from the [official Python website](https://www.python.org/downloads/).
2. Run the installer and make sure to check **"Add Python to PATH"** before clicking _Install Now_.
3. Verify the installation by opening **Command Prompt** and running:
   ```bash
   python --version
   ```

### macOS

Python 3 usually comes pre-installed on macOS, but it’s often outdated.
It’s recommended to install the latest version via Homebrew:

```bash
brew install python
```

Verify with:

```bash
python3 --version
```

### Linux

#### Debian/Ubuntu:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### Fedora:

```bash
sudo dnf install python3 python3-pip
```

Check Installation with:

```bash
python3 --version
```

Once installed, you can manage dependencies with:

```bash
pip install -r requirements.txt
```

## 📦 Installation

Clone the repository:

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

Count lines from all files except for `.css` files:

```bash
python3 lineCounter.py /path/to/project --exclude-ext .css
```

Count all files but skip certain directories:

```bash
python3 lineCounter.py /path/to/project --exclude node_modules venv
```

Combine directory and extension exclusion:

```bash
python3 lineCounter.py /path/to/project --exclude node_modules build --exclude-ext .txt .json
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
