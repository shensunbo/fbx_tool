import os
import sys

def find_header_files(directory):
    header_files = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".h"):
                header_files.add(file)
    return header_files

def extract_used_headers(file_path, max_lines=100):
    used_headers = set()
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for i, line in enumerate(file):
                if i >= max_lines:
                    break
                line = line.split('//', 1)[0].strip()
                if line.startswith('#include'):
                    parts = line.split(None, 1)
                    if len(parts) > 1:
                        filename = parts[1].strip('<>"\n')
                        used_headers.add(os.path.basename(filename))
    except IOError as e:
        print(f"Could not read file {file_path}: {e}")
    return used_headers

def find_unused_headers(directory):
    all_header_files = find_header_files(directory)
    used_headers = set()

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".h", ".cpp", ".c")):
                file_path = os.path.join(root, file)
                used_headers.update(extract_used_headers(file_path))

    unused_headers = all_header_files - used_headers
    return unused_headers

def main():
    if len(sys.argv) != 2:
        print("Usage: python header_file_find.py <directory>")
        return

    directory = sys.argv[1]
    unused_headers = find_unused_headers(directory)
    
    print("Unused headers:")
    for header in unused_headers:
        print(header)

if __name__ == "__main__":
    main()
