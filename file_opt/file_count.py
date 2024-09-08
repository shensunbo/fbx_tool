import os
import sys


def count_c_and_h_files(directory):
    c_count = 0
    h_count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.c'):
                c_count += 1
            elif file.endswith('.h'):
                h_count += 1

    return c_count, h_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/your/directory")
        return

    directory_path = sys.argv[1]

    c_files, h_files = count_c_and_h_files(directory_path)

    print(f"in '{directory_path}' :")
    print(f".c count: {c_files}")
    print(f".h count {h_files}")

if __name__ == "__main__":
    main()