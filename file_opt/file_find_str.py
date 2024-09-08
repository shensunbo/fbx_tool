import os
import sys
def search_files_with_string(directory, search_string):
    found_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        if search_string in line:
                            found_files.append(file_path)
                            break
            except IOError as e:
                print(f"Error reading file {file_path}: {e}")

    return found_files

def main():
    if len(sys.argv) != 3:
        print("Usage: python header_file_find.py <directory> <target>")
        return

    directory_path = sys.argv[1]
    search_string = sys.argv[2]
    found_files = search_files_with_string(directory_path, search_string)

    if found_files:
        print(f"Files containing '{search_string}':")
        for file_path in found_files:
            print(file_path)
    else:
        print(f"No files containing '{search_string}' found.")

if __name__ == "__main__":
    main()