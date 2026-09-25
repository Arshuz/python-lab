import sys

def get_pyramid(n, symbol = "*"):
    """
    NAME
        get_pyramid - Draws a pyramid of stars.
    
    SYPNOSIS
        get_pyramid(n, symbol = "*")

    DESCRIPTION
        Draws a pyramid of given symbol with the given number of rows.

    PARAMETERS
        n      (int) : The number of rows in the pyramid.
        symbol (str) : The symbol to use for drawing the pyramid.
    """
    # 1. Validate that 'n' is an integer (and exclude booleans)
    if not isinstance(n, int) or isinstance(n, bool):
        sys.stderr.write(f"[ERROR in pyramid.py]: Expected an integer for 'n', but got '{type(n).__name__}'.\n")
        return None

    # 2. Validate row count range
    if n <= 0:
        sys.stderr.write(f"[ERROR in pyramid.py]: Number of rows ('n') must be a positive integer.\n")
        return None

    # 3. Validate symbol argument
    if not isinstance(symbol, str) or len(symbol) == 0:
        sys.stderr.write(f"[ERROR in pyramid.py]: Symbol ('symbol') must be a non-empty string.\n")
        return None

    print()
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        symbols = symbol * (2 * i - 1)
        print(f"{spaces}{symbols}")
    return True

if __name__ == "__main__":
    # Example usage
    get_pyramid(5, symbol="#")
    get_pyramid(3, symbol="*")