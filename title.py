# needs dynamic width adjustment

import inspection.get_inspect
import sys
import shutil

def get_title(title, center = 0, border = "*"):
    """
    NAME
        get_title - Creates a stylized header banner for terminal outputs.
    
    SYPNOSIS
        get_title(title, center, *rest)

    DESCRIPTION
        Prints a text title surrounded by custom border characters.
        Can automatically center the output based on terminal width.
        Can point errors efficiently.

    PARAMETERS
        title  (str)    : The text string to display INSIDE the banner.
        center (int)    : State flag (0 to CENTER align, 1 for STANDARD alignment).
        rest  (tuple)  : Optional border decoration characters (1 or 2 parameters, more than 2 parameters are IGNORED).
    """
    # 1. Validate that 'title' is a valid string
    if not isinstance(title, str):
        sys.stderr.write(f"[ERROR in title.py]: Title ('title') must be a non-empty string.\n")
        return None

    # 2. Validate alignment flag
    if center not in (0, 1):
        sys.stderr.write(f"[ERROR in title.py]: Alignment flag ('center') must be either 0 (CENTER) or 1 (STANDARD).\n")
        return None

    # 3. Validate border characters
    if not isinstance(border, str) or len(border) == 0:
        sys.stderr.write(f"[ERROR in title.py]: Border character ('border') must be a non-empty string.\n")
        return None

    clean_title = title.strip().title()
    border = border[0]

    width = shutil.get_terminal_size().columns
    header = f"{border} {clean_title} {border}"
    border_len = len(header)
    border_str = border * border_len

    if center == 0:
        border_str = border_str.center(width)
        header = header.center(width)

    print(f"\n{border_str}")
    print(header)
    print(f"{border_str}")
    return True

if __name__ == "__main__":
    # Example usage
    get_title("Welcome to the Program", center=0, border="#")
    get_title("Error Log", center=1, border="!")