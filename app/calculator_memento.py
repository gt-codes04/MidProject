"""
Calculator state management using the Memento pattern.
"""

class CalculatorMemento:
    def __init__(self, calculations):
        self._state = calculations.copy()
    
    def get_state(self):
        return self._state