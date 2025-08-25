import os
import sys
import argparse

# ---------------------------
# Helpers
# ---------------------------

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
    
# ---------------------------
# Core Logic
# ---------------------------

def process_subdirectories(directory_path, extensions=None, include_hidden=False, excludes=None, exclude_exts=None):
    excludes = excludes or []
    exclude_exts = exclude_exts or []

    total_lines = 0
    lines_by_type = {}
    skipped_files = []

    for root, dirs, files in os.walk(directory_path):
        # Filter hidden and excluded directories
        if not include_hidden:
            dirs[:] = [d for d in dirs if not d.startswith('.')]
        dirs[:] = [d for d in dirs if d not in excludes]

        for file in files:
            if should_skip_file(file, extensions, include_hidden, excludes, exclude_exts):
                continue

            ext_match = get_extension(file)
            file_path = os.path.join(root, file)
            num_lines = count_lines_in_file(file_path)

            if num_lines is None:
                skipped_files.append(file_path)
                continue

            total_lines += num_lines
            lines_by_type[ext_match] = lines_by_type.get(ext_match, 0) + num_lines

    return total_lines, lines_by_type, skipped_files

# def count_total_lines(directory_path, extensions=None, include_hidden=False, excludes=None, exclude_exts=None):
#     print(f"Counting total lines of code in {directory_path}...")
#     total_lines, lines_by_type, skipped_files = process_subdirectories(
#         directory_path, extensions, include_hidden, excludes, exclude_exts
#     )

#     print(f"\nTotal lines of code: {total_lines}\n")

#     if lines_by_type:
#         print("Lines by file type:")
#         no_ext_count = lines_by_type.pop("No Extension", None)

#         for ext in sorted(lines_by_type):
#             print(f"{ext}: {lines_by_type[ext]}")

#         if no_ext_count is not None:
#             print(f"No Extension: {no_ext_count}")

#     if skipped_files:
#         print(f"\nSkipped {len(skipped_files)} non-text/binary files.")

# def process_subdirectories(directory_path, extensions=None, include_hidden=False, excludes=None, exclude_exts=None):
#     if excludes is None:
#         excludes = []
#     if exclude_exts is None:
#         exclude_exts = []

#     total_lines = 0
#     lines_by_type = {}
#     skipped_files = []

#     for root, dirs, files in os.walk(directory_path):
#         # Remove hidden directories if not included
#         if not include_hidden:
#             dirs[:] = [d for d in dirs if not d.startswith('.')]

#         # Apply directory exclusions
#         dirs[:] = [d for d in dirs if d not in excludes]

#         for file in files:
#             # Skip hidden files if not included
#             if not include_hidden and file.startswith('.'):
#                 continue

#             # Skip excluded files
#             if file in excludes:
#                 continue

#             # Skip excluded extensions (only matters if no --ext provided)
#             if extensions is None and any(file.lower().endswith(ext) for ext in exclude_exts):
#                 continue

#             # Extension filtering
#             if extensions is None:
#                 ext_match = os.path.splitext(file)[1].lower()
#                 if ext_match == "":
#                     ext_match = "No Extension"
#             else:
#                 ext_match = next((ext for ext in extensions if file.lower().endswith(ext)), None)
#                 if ext_match is None:
#                     continue

#             file_path = os.path.join(root, file)
#             try:
#                 with open(file_path, "r", encoding="utf-8") as f:
#                     num_lines = len(f.readlines())
#                     total_lines += num_lines
#                     lines_by_type[ext_match] = lines_by_type.get(ext_match, 0) + num_lines
#             except (UnicodeDecodeError, OSError):
#                 skipped_files.append(file_path)
#                 continue

#     return total_lines, lines_by_type, skipped_files

def main():
    parser = argparse.ArgumentParser(
        description="Count total lines of code in a directory.",
        epilog="Example: python lineCounter.py /my/code --ext .py .cs .js"
    )
    parser.add_argument("directory", nargs="?", help="Path to the directory to scan")
    parser.add_argument("--ext", nargs="+", default=None,
                        help="File extensions to include (e.g., --ext .py .cs). If not provided, all files are counted.")
    parser.add_argument("--include-hidden", action="store_true",
                        help="Include hidden files and directories (default: false)")
    parser.add_argument(
        "--exclude", nargs="+", default=[],
        help="Directories or files to exclude (e.g., --exclude node_modules venv README.md)"
    )

    parser.add_argument(
        "--exclude-ext", nargs="+", default=[],
        help="File extensions to exclude when scanning all files (e.g., --exclude-ext .log .csv)"
    )
    args = parser.parse_args()

    if not args.directory:
        parser.print_help()
        sys.exit(0)

    count_total_lines(args.directory, args.ext, args.include_hidden, args.exclude, args.exclude_ext)

if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:
        if e.code == 2: 
            sys.exit(2)
