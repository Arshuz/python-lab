import sys

def get_avg(*num):
    """
    NAME
        get_avg - Concludes the mathematical average of \"n\" of numbers. 
    
    SYPNOSIS
        get_avg(num)

    DESCRIPTION
        Can conclude mathematical average for infinity of numbers.

    PARAMETERS
        *num (float or tuple): The numbers for which to calculate the average.
    """
    try:
        if not num:
            raise ValueError("No numbers provided for average calculation.")
        avg = sum(num) / len(num)
        return avg
    except Exception as e:
        sys.stderr.write(f"[ERROR in average.py]: {e}\n")
        return None

if __name__ == "__main__":
    # Example usage
    average = get_avg(10, 20, 30, 40, 50)
    if average is not None:
        print(f"The average is: {average}")