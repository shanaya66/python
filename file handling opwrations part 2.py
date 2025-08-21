# 🌟 File Handling Project - Aesthetic Edition 🌟

# Write to the file
file = open("i_like_to_study.txt", "w")
file.write("📘 Learning Python file handling is fun!\n")
file.write("✨ Adding some cool lines into the file.\n")
file.write("🎮 Coding is like playing in creative mode!\n")
file.close()

print("✅ File has been written.\n")

# Read the file
print("📖 Reading file contents:\n")
file = open("i_like_to_study.txt", "r")
print(file.read())
file.close()

# Append to the file
file = open("i_like_to_study.txt", "a")
file.write("💡 Added more lines in Part 2!\n")
file.write("🌈 Keep going, you're doing amazing!\n")
file.close()

print("✅ File updated with new lines.\n")

# Show updated content
print("📘 Final file contents:\n")
file = open("i_like_to_study.txt", "r")
for line in file:
    print("👉", line.strip())
file.close()

