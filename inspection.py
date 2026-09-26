import sys

def get_inspect(var_name, var):
    """
    NAME
        get_inspect - Displays the values and the type of a variable neatly.
    
    SYPNOSIS
        get_inspect(var_name, var)

    DESCRIPTION
        Prints the variable name in a pair of square brackets.
        Prints the value(or)s of the variable as it contains.
        Prints the data type of the variable in neatly text.
        Prints all these information in one line.
        Can point errors efficiently.

    PARAMETERS
        var_name (str)  : The name of a variable which is to be examined and displayed inside a pair of square brackets \"[] \".
        var      (chr)  : The variable which contains the value(or)s. This parameter gives the data of the value(or)s and the data type.
    """
    # 1. Validate that var_name is a non-empty string
    if not isinstance(var_name, str) or not var_name.strip():
        sys.stderr.write("[ERROR in inspection.py]: 'var_name' must be a non-empty string.\n")
        return None

    var_type = type(var).__name__

    print(f"[{var_name.strip()}]  Value: {var} | Type: {var_type}")
    return True

if __name__ == "__main__":
    # Example usage
    get_inspect("my_variable", 42)
    get_inspect("my_list", [1, 2, 3])
    get_inspect("my_string", "Hello, World!")