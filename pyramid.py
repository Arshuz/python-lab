def get_pyramid(n, *rest):
    """
    NAME
        get_pyramid - Draws a pyramid of stars.
    
    SYPNOSIS
        get_pyramid(n, *rest)

    DESCRIPTION
        Draws a pyramid of given symbol with the given number of rows.

    PARAMETERS
        n  (int)  : The number of rows in the pyramid.
        *rest (str) : The symbol to use for drawing the pyramid.
    """
    if n <= 0:
        print("Error: Number of rows must be a positive integer.")
        return
    sym = rest[0] if rest else "*"
    print(f"\n")
    if len(rest) > 1:
        print(f"\nWARNING: THIS FUNCTION ONLY NEEDS ONE MUST PARAMETER AND ONE OPTIONAL PARAMETER!!!\n")
    for i in range(1, n + 1):
        print(" " * (n - i) + sym * (2 * i - 1))