import sys

def get_count(char, comment = None):
    """
    NAME
        get_count - Counts a string of characters.
    
    SYPNOSIS
        get_count(char, comment = None)

    DESCRIPTION
        Automatically remove leading and trailing whitespaces.
        Counts the number of characters present in the stripped string.
        Optionally appends a comment to the output.

    PARAMETERS
        char    (str)  : The character string to be counted WITHOUT leading and trailing WHITESPACES.
        comment (str)  : Optional comment to be displayed ALONG with the counted result AFTER \"# \" sequence. Does not take more than ONE parameter, others are IGNORED and prints a WARNING message.
    """
    # 1. Type validation to ensure char is a string
    if not isinstance(char, str):
        sys.stderr.write(f"[ERROR in counter.py]: Expected a string, but got type '{type(char).__name__}'.\n")
        return None

    clean_str = char.strip()
    str_length = len(clean_str)
    return str_length

if __name__ == "__main__":
    # Example usage
    count = get_count("   Hello, World!   ")
    print(f"Counted characters: {count}")