# Under_development

import os
import shutil
import signal
import time

def draw_screen():
    print("\033[H\033[J", end = "")
    width, height = shutil.get_terminal_size()
    print(f"The width is {width}\nThe height is {height}")

def handle_resize(signum, frame):
    draw_screen()

if __name__ == "__main__":
    if hasattr(signal, "SIGWINCH"):
        signal.signal(signal.SIGWINCH, handle_resize)

    draw_screen()

    try:
        print("\nPress \"Ctrl + C\" to exit...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting", end = "", flush = True)
        time.sleep(1)
        print(".", end = "", flush = True)
        time.sleep(1)
        print(".", end = "", flush = True)
        time.sleep(1)
        print(".", end = "", flush = True)
        print()