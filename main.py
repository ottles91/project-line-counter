import os
import sys

def count_total_lines(directory_path):
    print("Counting total lines of code...")
    total_lines = process_subdirectories(directory_path)
    print(f"Total lines of code: {total_lines}")
    
def process_subdirectories(directory_path):
    print("Processing subdirectories")
    total_lines = 0
    for root, _, files in os.walk(directory_path):
        for file in files:
            # print(f"Found file: {file}")
            if file.lower().endswith(".swift"):
                file_path = os.path.join(root, file)
                # print(f"Reading {file_path}")
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                    # print(f"  → {len(lines)} lines")
                    total_lines += len(lines)
    return total_lines

def main():
    if len(sys.argv) > 1:
        count_total_lines(sys.argv[1])
    else:
        count_total_lines(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    main()
    print("Finished!")