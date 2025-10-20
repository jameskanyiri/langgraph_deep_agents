from typing import Literal, Union


def calculator(
    operation: Literal["add", "subtract", "multiply", "divide"],
    a: Union[int, float],
    b: Union[int, float],
) -> Union[int, float]:
    
    """
    Define a calculator tool that can perform addition, subtraction, multiplication, and division.
    
    Args:
        operation (Literal["add", "subtract", "multiply", "divide"]): The operation to perform.
        a (Union[int, float]): The first number.
        b (Union[int, float]): The second number.
    
    Returns:
        Union[int, float]: The result of the operation.
    """
    
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
