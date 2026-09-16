def get_avg(first_num, *rest):
    """
    NAME
        get_avg - Concludes the mathematical average of \"n\" of numbers. 
    
    SYPNOSIS
        get_avg(first_num, *rest)

    DESCRIPTION
        Can conclude mathematical average for infinity of numbers.

    PARAMETERS
        first_num (float)  : The mandatory number which is needed so that this function does not end in error.
        *rest     (tuple)  : Optional tuple of empty to numerous of floating values (other factors, can be from 0 to infinity).
    """
    all_num = (first_num,) + rest
    return sum(all_num) / len(all_num)