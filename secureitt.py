import random
import string
import re

# Function to generate a strong password
def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Function to check password strength
def check_password_strength(password):
    score = 0
    if len(password) >= 12:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    if score == 5:
        return "Strong ✅"
    elif score >= 3:
        return "Medium ⚠️"
    else:
        return "Weak ❌  |  ⚠️  Warning: This password is too weak — don't use it!"

# Main menu
def main():
    while True:
        print("\n=== secureitt ===")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            length = int(input("Enter password length (default 16): ") or 16)
            new_pass = generate_password(length)
            print(f"\nGenerated Password: {new_pass}")
        elif choice == "2":
            pw = input("Enter password to check: ")
            result = check_password_strength(pw)
            print(f"\nStrength: {result}")
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
