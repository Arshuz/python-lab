import sys

def get_avg(num):
    """
    NAME
        get_avg - Concludes the mathematical average of \"n\" of numbers. 
    
    SYPNOSIS
        get_avg(num)

    DESCRIPTION
        Can conclude mathematical average for infinity of numbers.

    PARAMETERS
        num (float or tuple): The number or tuple of numbers for which to calculate the average.
    """
    try:
        if not num:
            raise ValueError("No numbers provided for average calculation.")
        avg = sum(num) / len(num)
        if __name__ == "__main__":
            print(f"The average of {num} is: {get_avg(num)}")
        else:
            return avg
    except Exception as e:
        sys.stderr.write(f"[ERROR in average.py]: {e}\n")
        return None

if __name__ == "__main__":
    # Example usage
    numbers = (10, 20, 30, 40, 50)
    average = get_avg(numbers)
    if average is not None:
        print(f"The average of {numbers} is: {average}")