import os
from .utilities import should_skip_file, get_extension, count_lines_in_file

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

def count_total_lines(directory_path, extensions=None, include_hidden=False, excludes=None, exclude_exts=None):
    """Run the scan and print results in a human-readable way."""
    print(f"Counting total lines of code in {directory_path}...")
    total_lines, lines_by_type, skipped_files = process_subdirectories(
        directory_path, extensions, include_hidden, excludes, exclude_exts
    )

    print(f"\nTotal lines of code: {total_lines}\n")

    if lines_by_type:
        print("Lines by file type:")
        no_ext_count = lines_by_type.pop("No Extension", None)

        for ext in sorted(lines_by_type):
            print(f"{ext}: {lines_by_type[ext]}")

        if no_ext_count is not None:
            print(f"No Extension: {no_ext_count}")

    if skipped_files:
        print(f"\nSkipped {len(skipped_files)} non-text/binary files.")