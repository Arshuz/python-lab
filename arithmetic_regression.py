import sys
from option import get_option

def get_arithmetic_regression():
    """
    NAME
        get_arithmetic_regression - Concludes arithmetic regression in Addition, Subtraction, Multiplication, Exponential, and Division with a list of numbers.
    
    SYPNOSIS
        get_arithmetic_regression()

    DESCRIPTION
        Returns calculated algebraic answer in Addition, Subtraction, Multiplication, Exponential, and Division with a list of numbers.
        Lets the user create a list of sequence number.
        Warns the user about the risk to their system if this program is misused.
        Can point errors efficiently.
    """
    ans = get_option("Which operator would you like to use?", 5, "Addition", "Subtraction", "Multiplication", "Exponential", "Division")
    if ans == 1:
        operator = "+"
        total = 0
    elif ans == 2:
        operator = "-"
        total = 0
    elif ans == 3:
        operator = "*"
        total = 1
    elif ans == 4:
        operator = "**"
        print("If sequence number starts from 1;")
        print("\tThe total will be 1 as per the mathematical rule:")
        print("\t\t1 ^ n  =  1\n")
        total = int(input("Enter a positive Natural number except 1: "))
    elif ans == 5:
        operator = "/"
        total = 1
    else:
        sys.stderr.write(f"[ERROR in arithmetic_regression.py]: get_option() function returned None.\n")
        return None

    # get_option("In what sequence would you like to perform the operation?", 5, "diff = 0 i.e. 1, 2, 3...", "diff = 1 i.e. 1, 3, 5...", "diff = 2 i.e. 1, 4, 7...", "diff = 3 i.e. 1, 5, 9...", "diff = n i.e. You can choose any number as the difference between the numbers in the sequence.")

    diff = int(input("Enter the difference between the numbers in the sequence: "))
    end = int(input("Enter the end number of the sequence: "))
    if 20 <= end < 25:
        print("\nBEWARE OF YOUR SYSTEM'S MEMORY AND COMPUTATIONAL POWER BEFORE EXECUTING THIS PROGRAM.\n")
    elif 25 <= end < 30:
        print("BEWARE OF YOUR SYSTEM'S MEMORY AND COMPUTATIONAL POWER BEFORE EXECUTING THIS PROGRAM.\n")
        confirmation = str(input(f"Are you sure about executing this program when end point is {end}? \"YES\" or \"NO\": "))

        if confirmation.upper() == "NO":
            print("")
            return None
        elif confirmation.upper() == "YES":
            pass
        else:
            sys.stderr.write("\n[ERROR in arithmetic_regression.py]: The confirmation flag must be \"YES\" or \"NO\"")
            print(f"You entered {confirmation}\n\n")
            return None

    elif end >= 30:
        print(f"\nWARNING: YOU ENTERED {end} IS ABOVE 30 WHICH IS A LIMIT TO STOP THIS PROGRAM ITSELF IMMEDIATELY.\n")
        print("YOU CAN CHANGE THIS CONFIGURATION IF YOUR SYSTEM CAN MANAGE ABOVE THE LIMIT '30'.")
        print("Browse to \"python-lab/arithmetic_regression.py\" in line 34. Change and set a new limit.\n")
        print("STOPPING .....\n")
        return None

    if not diff >= 0:
        sys.stderr.write("[ERROR in arithmetic_regression.py]: The difference must be a positive integer such as 0, 1, 2, ...\n")
        return None

    if not total < end:
        sys.stderr.write("[ERROR in arithmetic_regression.py]: The end point must not be less than or equal to the starting point.\n")
        return None

    seq = []
    for i in range(1, end+1, diff+1):
        seq.append(i)

    if __name__ == "__main__":
        print(f"Sequence is: {seq}\n")

    for i in range(len(seq)):
        if operator == "+":
            total += seq[i]
        elif operator == "-":
            total -= seq[i]
        elif operator == "*":
            total *= seq[i]
        elif operator == "**":
            total **= seq[i]
        elif operator == "/":
            total /= seq[i]
        else:
            sys.stderr.write(f"[ERROR in arithmetic_regression.py]: Invalid operator.\n")
            return None

    if __name__ == "__main__":
        print(f"Total is: {total}\n")

    return True

if __name__ == "__main__":
    get_arithmetic_regression()