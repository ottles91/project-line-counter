import os
import sys
import argparse

def count_total_lines(directory_path, extensions):
    print(f"Counting total lines of code in {directory_path}...")
    total_lines = process_subdirectories(directory_path, extensions)
    print(f"Total lines of code: {total_lines}")

def process_subdirectories(directory_path, extensions):
    total_lines = 0
    for root, _, files in os.walk(directory_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    total_lines += len(f.readlines())
    return total_lines


def main():
    parser = argparse.ArgumentParser(description="Count total lines of code in a directory.")
    parser.add_argument("directory", help="Path to the directory to scan")
    parser.add_argument("--ext", nargs="+", default=[".py", ".swift"],
                        help="File extensions to include (e.g., --ext .py .swift)")
    args = parser.parse_args()

    count_total_lines(args.directory, args.ext)

if __name__ == "__main__":
    main()
    print("Finished!")