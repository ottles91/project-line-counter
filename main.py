import os
import sys

def count_total_lines(start_directory):
    print("Counting total lines of code...")

def main():
    # NOTE: If you're not running with a command line argument then specify your pathname here

    # ADD YOUR DIRECTORY PATH HERE
    start_directory = ""

    if len(sys.argv) > 1:
        start_directory = sys.argv[1]

    count_total_lines(start_directory)

if __name__ == "__main__":
    main()
    print("Finished!")