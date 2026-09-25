import math
import sys
from average import get_avg

def get_binary_search(low_value, target_no, high_value):
    """
    NAME
        get_binary_search - Obtains the target number by reducing the search range half each time(Binary Search).
    
    SYPNOSIS
        get_binary_search(low_value, target_no, high_value)

    DESCRIPTION
        Sends an ERROR message if the target_no is OUT of range.
        FINDS the mid-point of the range and CONCLUDES if the target_no is mathematically close by to the mid-point.
        CHANGES the upper-bound or the lower-bound to the mid-point in according to in which range does the target_no LIVE in.

    PARAMETERS
        low_value  (float)  : The lower-bound of a range.
        target_no  (float)  : The target number to obtained by the help of this algorithm.
        high_value (float)  : The upper-bound of the range
    """
    # 1. Type validation to ensure numeric bounds
    if not all(isinstance(val, (int, float)) for val in (low_value, target_no, high_value)):
        sys.stderr.write("[ERROR in binary_search.py]: All parameters must be numeric (int or float).\n")
        return None

    # 2. Logic check: lower bound must be less than or equal to upper bound
    if low_value > high_value:
        sys.stderr.write("[ERROR in binary_search.py]: Invalid range (low_value cannot be greater than high_value).\n")
        return None

    # 3. Target out-of-bounds check
    if not (low_value <= target_no <= high_value):  
        sys.stderr.write("[ERROR in binary_search.py]: Target number is out of range.\n")
        return None

    avg = get_avg(low_value,high_value)
    if __name__ == "__main__":
        print(f"The  current  avg  is  {avg}")

    # Handle failure if get_avg returns None or non-numeric error
    if avg is None or not isinstance(avg, (int, float)):
        sys.stderr.write("[ERROR in binary_search.py]: Calculation aborted due to error in get_avg.\n")
        return None
    
    if math.isclose(avg, target_no, abs_tol = 1e-9):
        return avg
    elif avg < target_no:
        low_value = avg
        if __name__ == "__main__":
            print(f"Lower bound changes to {avg}")
    else:
        high_value = avg
        if __name__ == "__main__":
            print(f"Upper bound changes to {avg}")
    return get_binary_search(low_value, target_no, high_value)

if __name__ == "__main__":
    # Example usage
    result = get_binary_search(1, 9, 10)
    if result is not None:
        print(f"Found target: {result}")