from enum import Enum
import random

class Operations(Enum):
    ADD = 0
    SUBTRACT = 1
    MULTIPLY = 2
    DIVIDE = 3

    def __str__(self) -> str:
        match self:
            case self.ADD:
                return "+"
            case self.SUBTRACT:
                return "-"
            case self.MULTIPLY:
                return "*"
            case self.DIVIDE:
                return "/"
    
    def calculate(self, n1: float, n2: float) -> float:
        match self:
            case self.ADD:
                return n1 + n2
            case self.SUBTRACT:
                return n1-n2
            case self.MULTIPLY:
                return n1*n2
            case self.DIVIDE:
                return n1/n2

def random_operation() -> Operations:
    return random.choice(list(Operations))