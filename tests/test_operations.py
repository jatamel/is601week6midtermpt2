from decimal import Decimal
from typing import Callable
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
import pytest

def test_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal], expected):
    '''Testing various operations'''
    calculation = Calculation.create(a= Decimal, b= Decimal, operation = operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"

# Keeping the divide by zero test as is since it tests a specific case
def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
