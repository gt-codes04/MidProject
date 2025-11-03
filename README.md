# 🧮 Enhanced Calculator Command-Line Application

![CI](https://github.com/gt-codes04/MidProject/actions/workflows/python-app.yml/badge.svg)

## 📘 Overview
This is a **fully functional, object-oriented command-line calculator** built for the NJIT Midterm Project.  
It features **modular design**, **error handling**, **logging**, **undo/redo (Memento pattern)**, **auto-save (Observer pattern)**, and a **Factory-based operation system**.  
All functionality is covered by **pytest** with >90% coverage, and **GitHub Actions** runs CI on every push.

---

## ⚙️ Features
### Core Operations
- ➕ Addition, ➖ Subtraction, ✖️ Multiplication, ➗ Division  
- 🔢 Power, Root, Modulus, Integer Division  
- 💯 Percentage and Absolute Difference  

### Advanced Functionality
- 🧠 Undo / Redo with **Memento pattern**
- 📜 Persistent History using **pandas**
- 📡 Observers for auto-save and logging
- ⚙️ Configurable via `.env` file
- 🧩 Factory pattern for operation creation
- 🧾 Robust logging and input validation

---

## 📁 Project Structure
mid_calculator/
├── app/
│ ├── init.py
│ ├── calculator.py
│ ├── calculation.py
│ ├── calculator_config.py
│ ├── calculator_memento.py
│ ├── exceptions.py
│ ├── history.py
│ ├── input_validators.py
│ ├── logger.py
│ └── operations.py
├── tests/
│ ├── test_calculator.py
│ ├── test_calculation.py
│ ├── test_operations.py
│ ├── test_history.py
│ ├── test_validators.py
│ └── test_memento_extra.py
├── .env
├── requirements.txt
├── pytest.ini
├── .gitignore
└── .github/workflows/python-app.yml