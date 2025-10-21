🔐 SecureIt-Py — Password Generator & Breach Checker

SecureIt-Py is a lightweight yet powerful Python tool that can:

Generate strong random passwords

Check if a password has been leaked in data breaches

Evaluate password strength

Protect your privacy using k-Anonymity

🚀 Features

✅ Secure Random Generation using Python’s secrets module
✅ Password Strength Evaluation — checks for length, complexity & diversity
✅ Breach Check via HaveIBeenPwned API

✅ k-Anonymity Protection — only partial SHA-1 hash is sent to the API
✅ Fast CLI Interface — works directly from your terminal

⚙️ Tech Stack

Language: Python 3.x

Libraries: requests, hashlib, secrets, string

🧠 How It Works

The tool generates a password using cryptographically secure randomness.

When checking, it hashes the password with SHA-1.

Only the first 5 characters of the hash are sent to the API.

The API returns a list of matching suffixes.

The tool checks locally if your password’s hash appears in that list.

If found → ⚠️ “This password has been leaked — DO NOT USE IT!”

If not found but weak → ⚠️ “This password wasn’t found but is still weak — avoid using it.”

If strong → ✅ “Password is safe and strong.”

💻 Usage
🔸 Install dependencies
pip install requests

🔸 Run the script
python secureit.py

🔸 Example output
Generated Password: X@9zK!t7QeR2
Strength: Very Strong 💪
Checking breaches...
⚠️ Warning: This password has appeared 10 times in known breaches. DO NOT USE IT!

🧩 Code Structure
secureit.py
│
├── generate_password()   # Generates secure random password
├── evaluate_strength()   # Analyzes password complexity
├── check_pwned()         # Checks HaveIBeenPwned API
└── main()                # CLI interface

🔒 Privacy Note

Your password is never sent to any server.
Only the first 5 characters of its SHA-1 hash are used for lookup, ensuring complete anonymity.

👨‍💻 Author

Yousef Magdy Hassan
GitHub: @joeauraa
