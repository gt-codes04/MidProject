# Calculator Application

A simple yet powerful calculator application with memory functionality, operation history, and extensive error handling.

## Features

- Basic arithmetic operations (+, -, *, /)
- Expression validation
- Operation history tracking
- State management (Memento pattern)
- Logging functionality
- Environment-based configuration

## Project Structure

```
project_root/
├── app/                 # Main application package
├── tests/              # Test files
├── .env                # Environment configuration
├── requirements.txt    # Project dependencies
└── .github/workflows/  # CI/CD configuration
```

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

```python
from app.calculator import Calculator

calc = Calculator()
result = calc.calculate("2 + 2")
print(result)  # Output: 4
```

## Testing

Run the tests using:
```
python -m unittest discover tests
```

## License

MIT License