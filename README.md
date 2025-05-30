# 📦 Package Stack Category (Python)

A simple Python script that determines whether a package is **STANDARD**, **SPECIAL**, or **REJECTED** based on its dimensions and mass.  Contains a suite of tests that assert expected outputs given fixed inputs.

## 🏃 How to Run

```bash
python3 package_stack_category.py
```

## If all Tests Pass the output will be
```
main
all tests passed!
```

## What it Does

- Checks if a package is bulky (based on volume or dimensions)
- Checks if it's heavy (mass > 20 kg)
- Assigns a category using basic rules:
 - Not bulky and not heavy -> STANDARD
 - bulky and heavy -> REJECTED
 - Else -> SPECIAL
