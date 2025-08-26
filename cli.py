import sys
import argparse
from .counter import count_total_lines

def main():
    parser = argparse.ArgumentParser(
        description="Count total lines of code in a directory.",
        epilog="Example: python -m LineCounter /my/code --ext .py .cs .js"
    )
    parser.add_argument(
        "directory",
        nargs="?",
        help="Path to the directory to scan"
    )
    parser.add_argument(
        "--ext",
        nargs="+",
        default=None,
        help="File extensions to include (e.g., --ext .py .cs). "
             "If not provided, all text-based files are counted."
    )
    parser.add_argument(
        "--include-hidden",
        action="store_true",
        help="Include hidden files and directories (default: false)"
    )
    parser.add_argument(
        "--exclude",
        nargs="+",
        default=[],
        help="Directories or files to exclude (e.g., --exclude node_modules venv README.md)"
    )
    parser.add_argument(
        "--exclude-ext",
        nargs="+",
        default=[],
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