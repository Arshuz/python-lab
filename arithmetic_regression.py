import sys
from option import get_option

def get_arithmetic_regression():
    get_option("Which operator would you like to use?", 5, "Addition", "Subtraction", "Multiplication", "Exponential")
    get_option("Which operator would you like to use?", 5, "Addition", "Subtraction", "Multiplication", "Exponential", "Division")
    return True