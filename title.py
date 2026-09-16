# needs dynamic width adjustment

from inspection import get_inspect
import shutil

def get_title(title, center, *rest):
    """
    NAME
        get_title - Creates a stylized header banner for terminal outputs.
    
    SYPNOSIS
        get_title(title, center, *rest)

    DESCRIPTION
        Prints a text title surrounded by custom border characters.
        Can automatically center the output based on terminal width.

    PARAMETERS
        title  (str)    : The text string to display INSIDE the banner.
        center (int)    : State flag (0 to CENTER align, 1 for STANDARD alignment).
        *rest  (tuple)  : Optional border decoration characters (1 or 2 parameters, more than 2 parameters are IGNORED).
    """
    # get_inspect("*rest", rest)
    width = shutil.get_terminal_size().columns
    if not rest:
        header = title.strip().title()
        if center == 0:
            header = header.center(width)
        print(f"\n{header}")
        return 0
    elif len(rest) < 2:
        item = rest[0]
        if not item:
            item = "*"
        top_rep = len(title.strip()) + len(item) * 2 + 2
        border = item[0] * top_rep
        header = (f"{item} {title.strip().upper()} {item}")
    else:
        top_rep = len(title.strip()) + len(rest[1]) * 2 + 2
        border = rest[0] * top_rep
        header = (f"{rest[1]} {title.strip().upper()} {rest[1]}")

    if center == 0:
        border = border.center(width)
        header = header.center(width)

    _output(border, header)
    return border, header

def _output(border, header):
    print(f"\n{border}")
    print(f"{header}")
    print(f"{border}")
    return 0