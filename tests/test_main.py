"""
This module tests the main application functionality, ensuring that arithmetic operations are performed
correctly when interacting with user input and command-line arguments.
"""
import pytest
from main import calculate_and_print  # Ensure this import matches your project structure

# Parameterize the test function to cover different operations and scenarios, including errors
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'addition', "The result of 5 addition 3 is equal to 8"),  # Updated 'add' to 'addition'
    ("10", "2", 'subtraction', "The result of 10 subtraction 2 is equal to 8"),  # Updated 'subtract' to 'subtraction'
    ("4", "5", 'multiplication', "The result of 4 multiplication 5 is equal to 20"),  # Updated 'multiply' to 'multiplication'
    ("20", "4", 'division', "The result of 20 division 4 is equal to 5"),  # Updated 'divide' to 'division'
    ("1", "0", 'division', "An error occurred: Cannot divide by zero"),  # Adjusted for the actual error message
    ("9", "3", 'unknown', "Unknown operation: unknown"),  # Test for unknown operation
    ("a", "3", 'addition', "Invalid number input: a or 3 is not a valid number."),  # Testing invalid number input
    ("5", "b", 'subtraction', "Invalid number input: 5 or b is not a valid number.")  # Testing another invalid number input
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    """
    Test the calculate_and_print function with various inputs and operations.

    Parameters:
    a_string (str): The first operand as a string.
    b_string (str): The second operand as a string.
    operation_string (str): The operation to perform.
    expected_string (str): The expected result.
    capsys: Pytest fixture to capture standard output.
    """
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string
