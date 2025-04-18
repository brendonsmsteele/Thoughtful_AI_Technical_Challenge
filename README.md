# 📦 Package Stack Category (Python)

A simple Python script that determines whether a package is **STANDARD**, **SPECIAL**, or **REJECTED** based on its dimensions and mass.

## 🏃 How to Run

```bash
python3 package_stack.py
```

## If all Tests Pass the output will be
main
all tests passed!

## What it Does

- Checks if a package is bulky (based on volume or size)
- Checks if it's heavy (mass > 20 kg)
- Assigns a category using basic rules:
 - Not bulky and not heavy -> STANDARD
 - bulky and heavy -> REJECTED
 - Else -> SPECIAL