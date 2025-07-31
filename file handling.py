# 📁 File Handling – Access Modes
# Created by: [Your Name]
# Date: July 24, 2025

def write_mode():
    with open("sample.txt", "w") as file:
        file.write("🌟 This is written in WRITE mode.\n")
    print("✅ Wrote to file in write mode.")

def append_mode():
    with open("sample.txt", "a") as file:
        file.write("➕ This is added using APPEND mode.\n")
    print("✅ Appended content in append mode.")

def read_mode():
    with open("sample.txt", "r") as file:
        content = file.read()
    print("📖 Reading file in READ mode:\n")
    print(content)

def read_write_mode():
    with open("sample.txt", "r+") as file:
        file.write("✍️ Modified using READ+WRITE mode.\n")
        file.seek(0)
        updated = file.read()
    print("🔁 File after read+write mode:\n")
    print(updated)

def main():
    print("╔════════════════════════════════════╗")
    print("║     📂 File Access Modes in Python  ║")
    print("║         (Read, Write, Append)      ║")
    print("╚════════════════════════════════════╝\n")

    write_mode()
    append_mode()
    read_mode()
    read_write_mode()

if __name__ == "__main__":
    main()
