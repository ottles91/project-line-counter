import os
import sys
import argparse

def count_total_lines(directory_path, extensions, include_hidden=False):
    print(f"Counting total lines of code in {directory_path}...")
    total_lines = process_subdirectories(directory_path, extensions, include_hidden)
    print(f"Total lines of code: {total_lines}")

def process_subdirectories(directory_path, extensions=None, include_hidden=False):
    total_lines = 0
    for root, dirs, files in os.walk(directory_path):
        if not include_hidden:
            dirs[:] = [d for d in dirs if not d.startswith('.')]

        for file in files:
            if not include_hidden and file.startswith('.'):
                continue
            if extensions is None or any(file.lower().endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    total_lines += len(f.readlines())
    return total_lines


def main():
    parser = argparse.ArgumentParser(
        description="Count total lines of code in a directory.",
        epilog="Example: python main.py /my/code --ext .py .cs .js"
    )
    parser.add_argument("directory", nargs="?", help="Path to the directory to scan")
    parser.add_argument("--ext", nargs="+", default=None,
                        help="File extensions to include (e.g., --ext .py .cs). If not provided, all files are counted.")
    parser.add_argument("--include-hidden", action="store_true",
                        help="Include hidden files and directories (default: false)")

    args = parser.parse_args()

    if not args.directory:
        parser.print_help()
        sys.exit(0)

    count_total_lines(args.directory, args.ext if args.ext else [".py", ".cs"], args.include_hidden)

if __name__ == "__main__":
    try:
        main()
        print("Finished!")
    except SystemExit as e:
        if e.code == 2: 
            sys.exit(2)

