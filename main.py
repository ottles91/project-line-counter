import os
import sys

def count_total_lines(directory_path):
    print("Counting total lines of code...")
    total_lines = process_subdirectories(directory_path)
    print(f"Total lines of code: {total_lines}")

    
def process_subdirectories(directory_path):
    total_lines = 0
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):  # Update later to improve filtering
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                    total_lines += len(lines)
    return total_lines


def main():
    # NOTE: If you're not running with a command line argument then specify your pathname here
    start_directory = ""

    if len(sys.argv) > 1:
        start_directory = sys.argv[1]
    else:
        start_directory = os.path.dirname(os.path.abspath(__file__))

    count_total_lines(start_directory)

if __name__ == "__main__":
    main()
    print("Finished!")