from dataclasses import dataclass
from typing import Callable, Dict
from . import operations as ops
from .exceptions import OperationError

@dataclass
class Calculation:
    operation_name: str
    a: float
    b: float
    operation: Callable[[float, float], float]
    def get_result(self) -> float:
        return self.operation(self.a, self.b)

class CalculationFactory:
    _mapping: Dict[str, Callable[[float, float], float]] = {
        "add": ops.add, "subtract": ops.subtract, "multiply": ops.multiply,
        "divide": ops.divide, "power": ops.power, "root": ops.root,
        "modulus": ops.modulus, "int_divide": ops.int_divide, "percent": ops.percent,
        "abs_diff": ops.abs_diff,
    }

    @classmethod
    def create(cls, op_name: str, a: float, b: float) -> Calculation:
        op = cls._mapping.get(op_name)
        if not op:
            raise OperationError(f"Unsupported operation: {op_name}")
        return Calculation(op_name, a, b, op)
