import sys

def get_option(question: str, option_count: int, *rest: str):
    
    if __name__ == "__main__":
        print(f"len of rest is: {len(rest)}\n")

    if option_count != len(rest):
        sys.stderr.write(f"[ERROR in option.py]: Number of options does not match number of option messages.\n")
        return None
        
    if len(question.strip()) == 0:
        sys.stderr.write(f"[ERROR in option.py]: There is no question.\n")
        return None

    if __name__ == "__main__":
        print(f"option_count is: {option_count}\n")
    
    if option_count <= 1:
        sys.stderr.write(f"[ERROR in option.py]: Option.py module cannot be used if there is zero or one option.\n")
        return None

    if not all(isinstance(val, str) for val in (question, *rest)):
        sys.stderr.write(f"[ERROR in option.py]: question and rest parameters must be a string.\n")
        return None

    if not isinstance(option_count, int):
        sys.stderr.write(f"[ERROR in option.py]: option_count parameter must be an integer.\n")
        return None

    print(f"{question.strip().capitalize()}")
    for i in range(option_count):
        print(f"{i+1}. {rest[i]}")
    ans = int(input("\nEnter your choice: "))
    
    if __name__ == "__main__":
        print(f"Answer is: {ans}\n")

    if not 1 <= ans <= option_count:
        sys.stderr.write(f"[ERROR in option.py]: Your choice is out-of-bound.\n")
        return None

    return ans

if __name__ == "__main__":
    get_option("where is the key?", 3, "At the table", "Under the table", "Over the table")