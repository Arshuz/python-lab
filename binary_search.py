import math
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
    if not (low_value <= target_no <= high_value):
        return "Error: Target number is out of range, please check again"

    while True:
        avg = get_avg(low_value,high_value)
        # print(f"The  current  avg  is  {avg}")
        
        if math.isclose(avg, target_no, abs_tol = 1e-9):
            return avg
        elif avg < target_no:
            low_value = avg
            # print(f"Lower bound changes to {avg}")
        else:
            high_value = avg
            # print(f"Upper bound changes to {avg}")
    return 0
        