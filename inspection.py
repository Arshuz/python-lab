def get_inspect(var_name, var):
    """
    NAME
        get_inspect - Displays the values and the type of a variable neatly.
    
    SYPNOSIS
        get_title(var_name, var)

    DESCRIPTION
        Prints the variable name in a pair of square brackets.
        Prints the value(or)s of the variable as it contains.
        Prints the data type of the variable in neatly text.
        Prints all these information in one line.

    PARAMETERS
        var_name (str)  : The name of a variable which is to be examined and displayed inside a pair of square brackets \"[] \".
        var      (chr)  : The variable which contains the value(or)s. This parameter gives the data of the value(or)s and the data type.
    """
    print(f"[{var_name}]  Value: {var} | Type: {type(var).__name__}")
    return 0