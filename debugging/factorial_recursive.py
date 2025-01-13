#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function to calculate the factorial of a given number using recursion.
    
    Parameters:
    n (int): The number for which the factorial is to be calculated.
    
    Returns:
    int: The factorial of the number `n`. If `n` is 0, returns 1 (base case).
    """
    if n == 0:  # Base case: 0! is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!

# Read the input number from command-line argument and calculate its factorial
f = factorial(int(sys.argv[1]))
print(f)  # Print the calculated factorial

