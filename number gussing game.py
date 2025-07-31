# 🎲 Number Guessing Game 🎲

import random

print("🎉 Welcome to the Number Guessing Game! 🎉")
print("I'm thinking of a number between 1 and 100... can you guess it? 🤔")

# Generate random number
secret_number = random.randint(1, 100)

# Try to guess!
guesses = []

while True:
    guess = int(input("👉 Enter your guess: "))
    guesses.append(guess)

    if guess == secret_number:
        print(f"🎯 Bingo! You got it in {len(guesses)} tries! 🥳")
        break
    elif guess < secret_number:
        print("📈 Too low! Try a bigger number.")
    else:
        print("📉 Too high! Try a smaller number.")

print(f"🔁 Your guesses were: {guesses}")
