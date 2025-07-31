# 🌸🌼 Tulip Word to Letter List 🌼🌸
# A cute pastel-style breakdown of the word "tulip" into letters 💖

# 🌷 Original word
word = "tulip"

# 🍭 Turn word into list of letters
letter_list = list(word)

# 🌈 Print each letter in a soft aesthetic way
print("💌 The word 'tulip' becomes:")
print("🌸 [", end="")
for i, letter in enumerate(letter_list):
    pastel_letter = f"'{letter}'"
    if i < len(letter_list) - 1:
        print(pastel_letter, end=", ")
    else:
        print(pastel_letter, end="")
print("] 🌸")
