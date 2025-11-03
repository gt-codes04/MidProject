# Advanced Python Calculator

## Overview
This project is an object-oriented command-line calculator built using Python.  
It demonstrates key software engineering concepts such as modular programming, configuration management, and automated testing.  
The application integrates multiple design patterns, including Factory, Memento, and Observer, to ensure scalability and maintainability.

The calculator supports advanced arithmetic operations, undo/redo functionality, persistent history management, logging, and a user-friendly command-line interface (REPL).  
All code is tested using pytest with more than 90% coverage, and the CI/CD pipeline runs automatically via GitHub Actions.

---

## Features

### Core Functionality
- Standard operations: addition, subtraction, multiplication, division
- Advanced operations:
  - Power
  - Root
  - Modulus
  - Integer Division
  - Percentage Calculation
  - Absolute Difference
- Command-line REPL for interactive usage

### History Management
- Undo and Redo implemented using the Memento Design Pattern
- Persistent history management using CSV files
- Auto-saving of history enabled through observers

### Observer Pattern
- LoggingObserver: records all calculations to a log file
- AutoSaveObserver: automatically saves calculation history to CSV after every calculation

### Configuration Management
- Uses a `.env` file to manage environment-specific variables
- Controlled via `python-dotenv`
- Default configuration values are provided if the `.env` file is missing

### Error Handling
- Custom exceptions for invalid inputs and operations
  - ValidationError
  - OperationError
  - InsufficientOperandsError
- Graceful handling of divide-by-zero and invalid numeric inputs

### Logging
- Comprehensive logging implemented using Python’s built-in `logging` module
- Logs stored in the directory specified by `CALCULATOR_LOG_DIR`
- Includes operation names, operands, results, and timestamps

### Command-Line Interface (REPL)
Run the calculator interactively:
```bash
python -m app.calculator
Supported commands:

bash
Copy code
add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff
history, clear, undo, redo, save, load, help, exit
Project Structure
markdown
Copy code
project_root/
├── app/
│   ├── __init__.py
│   ├── calculator.py
│   ├── calculation.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   ├── operations.py
│   └── logger.py
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   ├── test_calculation.py
│   ├── test_operations.py
│   ├── test_history.py
│   └── test_validators.py
├── .env
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── python-app.yml
Testing
All modules are tested using pytest and pytest-cov.

To run tests locally:

bash
Copy code
pytest --cov=app --cov-fail-under=90
This command ensures that total coverage remains above 90%.
If coverage drops below the threshold, the CI/CD pipeline will fail automatically.

Continuous Integration (CI)
GitHub Actions is used for continuous integration.
The workflow file .github/workflows/python-app.yml automatically runs tests and enforces the coverage threshold whenever new commits or pull requests are pushed to the main branch.

CI Pipeline Steps:

Checkout repository

Set up Python environment

Install dependencies

Run all tests with pytest and coverage enforcement

Configuration (.env File)
Below is an example of the .env file used for configuration:

ini
Copy code
CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_MAX_HISTORY_SIZE=1000
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=6
CALCULATOR_MAX_INPUT_VALUE=1e12
CALCULATOR_DEFAULT_ENCODING=utf-8
CALCULATOR_LOG_FILE=calculator.log
CALCULATOR_HISTORY_FILE=history.csv
Each variable controls an aspect of the application’s behavior:

Directories: specify where logs and history are stored

Calculation Settings: control precision and input limits

Auto-Save: toggles automatic saving of history files

Installation
Step 1: Clone the repository
bash
Copy code
git clone https://github.com/gt-codes04/MidProject.git
cd MidProject
Step 2: Create a virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate        # For Windows
source venv/bin/activate     # For macOS/Linux
Step 3: Install dependencies
bash
Copy code
pip install -r requirements.txt
Step 4: Run the calculator
bash
Copy code
python -m app.calculator
Design Patterns Used
Pattern	Purpose
Factory	Creates and manages operation instances dynamically
Memento	Enables undo/redo functionality by storing state snapshots
Observer	Updates logs and saves history automatically on each calculation
Command-Line REPL	Provides interactive user input handling

Technologies Used
Python 3.10+

Pytest and Pytest-Cov

Pandas

Python-dotenv

Logging module

GitHub Actions for CI/CD

Author
Guna Teja Abdas
New Jersey Institute of Technology
GitHub: gt-codes04

