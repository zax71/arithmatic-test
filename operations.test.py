import unittest
from operations import Operations
import operations

class TestOperations(unittest.TestCase):
    _n1: float = 3.0
    _n2: float = 4.0
    def test_add_str(self):
        self.assertEqual(str(Operations.ADD), "+")
    
    def test_add_calculate(self):
        self.assertEqual(Operations.ADD.calculate(self._n1, self._n2), self._n1+self._n2)
    
    def test_subtract_str(self):
        self.assertEqual(str(Operations.SUBTRACT), "-")
    
    def test_subtract_calculate(self):
        self.assertEqual(Operations.SUBTRACT.calculate(self._n1, self._n2), self._n1-self._n2)
    
    def test_multiply_str(self):
        self.assertEqual(str(Operations.MULTIPLY), "*")
    
    def test_multiply_calculate(self):
        self.assertEqual(Operations.MULTIPLY.calculate(self._n1, self._n2), self._n1*self._n2)
    
    def test_divide_str(self):
        self.assertEqual(str(Operations.DIVIDE), "/")
    
    def test_divide_calculate(self):
        self.assertEqual(Operations.DIVIDE.calculate(self._n1, self._n2), self._n1/self._n2)
    
    def test_random_operation(self):
        self.assertIn(
            operations.random_operation(),
            [
                Operations.ADD,
                Operations.SUBTRACT,
                Operations.MULTIPLY,
                Operations.DIVIDE
            ]
        )

if __name__ == '__main__':
    unittest.main()