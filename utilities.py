import os

def should_skip_file(file, extensions, include_hidden, excludes, exclude_exts):
    """Return True if the file should be skipped based on rules."""
    if not include_hidden and file.startswith('.'):
        return True
    if file in excludes:
        return True
    if extensions is None and any(file.lower().endswith(ext) for ext in exclude_exts):
        return True
    if extensions is not None and not any(file.lower().endswith(ext) for ext in extensions):
        return True
    return False

def get_extension(file):
    """Return normalized extension, or 'No Extension' if missing."""
    ext = os.path.splitext(file)[1].lower()
    return ext if ext else "No Extension"


def count_lines_in_file(file_path):
    """Return number of lines in a text file, or None if unreadable/binary."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return len(f.readlines())
    except (UnicodeDecodeError, OSError):
        return None