# recursion.py
# Example of a recursive function to calculate factorial

def factorial(n):
    """Returns factorial of n using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Test
if __name__ == "__main__":
    print("Factorial of 5 is:", factorial(5))
