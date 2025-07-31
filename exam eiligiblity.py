# 📅 Exam Eligibility Checker 💻
import datetime

print("🎓✨ Welcome to the Exam Eligibility Portal ✨🎓")
print("Please enter your details to check if you're eligible! 📝")

name = input("Enter your name: ")
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

# Convert input to date
dob = datetime.datetime.strptime(dob_input, "%Y-%m-%d").date()
today = datetime.date.today()

# Calculate age
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

print(f"\n👤 Name: {name}")
print(f"🎂 Age: {age} years")

# Eligibility check
if age >= 18:
    print("✅ You are eligible to apply for the exam. Good luck! 💪")
else:
    print("❌ Sorry, you must be 18 or older to apply. Keep shining and try again soon 🌟")
