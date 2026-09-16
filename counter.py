def get_count(char, *rest):
    """
    NAME
        get_count - Counts a string of characters.
    
    SYPNOSIS
        get_count(char, *rest)

    DESCRIPTION
        Can automatically remove leading and trailing indents.
        Counts the number of characters present in a string.
        Lets to append comment along to the result.

    PARAMETERS
        char   (str)    : The character string to be counted WITHOUT leading and trailing INDENTS.
        *rest  (tuple)  : Optional comment to be displayed ALONG with the counted result AFTER \"# \" sequence. Does not take more than ONE parameter, others are IGNORED and prints a WARNING message.
    """
    if not rest:
        print(f"The count of {char.strip()} string is {len(char.strip())}")
        return 0
    elif len(rest) > 1:
        _solution(char, rest)
        print(f"\nWARNING: THIS FUNCTION ONLY NEEDS ONE MUST PARAMETER AND ONE OPTIONAL PARAMETER!!!\n")
        return char, rest
    else:
        _solution(char, rest)
        return char, rest

def _solution(char, rest):
    print(f"The count of {char.strip()} string is {len(char.strip())} # {rest[0]}")
    return 0