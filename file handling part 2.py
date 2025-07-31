# 📄 File Handling - Operations Part 1
# Topic: Reading a file in different ways
# Created by: [Your Name]
# Date: July 26, 2025

def create_sample_file():
    with open("readme.txt", "w") as file:
        file.write("Line 1: Welcome to File Handling!\n")
        file.write("Line 2: This file will be read in different ways.\n")
        file.write("Line 3: Python makes file I/O super easy.\n")
        file.write("Line 4: Let's explore all reading modes!\n")
    print("✅ Sample file 'readme.txt' created.\n")

def read_entire_content():
    print("🔹 Reading entire content using `.read()`:\n")
    with open("readme.txt", "r") as file:
        content = file.read()
        print(content)
    print("────────────────────────────────────────────\n")

def read_line_by_line():
    print("🔹 Reading line by line using `.readline()`:\n")
    with open("readme.txt", "r") as file:
        line = file.readline()
        while line:
            print(line.strip())
            line = file.readline()
    print("────────────────────────────────────────────\n")

def read_all_lines_list():
    print("🔹 Reading all lines into list using `.readlines()`:\n")
    with open("readme.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
    print("────────────────────────────────────────────\n")

def main():
    print("╔══════════════════════════════════════════╗")
    print("║    📘 File Handling – Operations Part 1    ║")
    print("║         Python Reading Methods Demo      ║")
    print("╚══════════════════════════════════════════╝\n")

    create_sample_file()
    read_entire_content()
    read_line_by_line()
    read_all_lines_list()

if __name__ == "__main__":
    main()
