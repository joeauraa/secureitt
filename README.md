# SecureIt-Py — Password Generator & Breach Checker

**SecureIt-Py** is a lightweight Python CLI tool that helps you:
- Generate strong random passwords.
- Evaluate password strength locally.
- (Optional) Check whether a password has appeared in known data breaches using HaveIBeenPwned k-Anonymity (not enabled by default).

---

## Features

- 🔒 Secure random generation using Python standard library.
- 🧠 Local strength evaluation with clear scoring and recommendations.
- ⚠️ Strong warnings for weak passwords that advise: **DO NOT USE**.
- 🚫 No external calls by default — privacy-preserving.
- ✅ Single-file distribution for easy deployment.

---

## Quick Start

### Requirements
- Python 3.8 or newer

### Install
```bash
git clone https://github.com/<USERNAME>/SecureIt-Py.git
cd SecureIt-Py
```

### Run
```bash
python password_tool.py
```

You'll see an interactive menu:
```
Password Tool — Generator & Strength Checker
Menu:
  1) Generate Password
  2) Check Password Strength
  3) Print README
  4) Exit
```

---

## How Strength Is Evaluated

The tool assigns up to 5 points:
- Length >= 12 -> 1 point
- Uppercase + lowercase -> 1 point
- Digits -> 1 point
- Symbols -> 1 point
- (Implicit) composition -> counts toward overall score

Score interpretation:
- 5 -> Very Strong
- 4 -> Strong
- 3 -> Fair
- 0-2 -> Weak (explicit DO NOT USE warning)

---

## Optional: Add Breach Check (HaveIBeenPwned)

If you want to enable breach checking, add a function that:
- Computes SHA-1 of the password,
- Sends the first 5 chars of the hash to HIBP range API,
- Parses results locally to determine occurrence count.

Be careful with network calls and follow HIBP usage guidelines.

---

## License

MIT-style — use, modify, and redistribute freely.

---

## Author

Yousef Magdy Hassan — Python Developer & Security Enthusiast  
GitHub: https://github.com/joeauraa
