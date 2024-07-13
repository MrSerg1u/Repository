import os
import sys
import time

def count_occurrences(input_directory, search_strings):
    occurrences = {string: 0 for string in search_strings}

    for root, _, files in os.walk(input_directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    for string in search_strings:
                        occurrences[string] += line.count(string)

    return occurrences

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 line-reader.py <input-directory> <string1> <string2> ... <stringn>")
        sys.exit(1)

    input_directory = sys.argv[1]
    search_strings = sys.argv[2:]

    start_time = time.time()

    occurrences = count_occurrences(input_directory, search_strings)

    end_time = time.time()
    elapsed_time = end_time - start_time

    for string, count in occurrences.items():
        print(f"{string} : {count} occurrences!")

    print(f"Execution time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
