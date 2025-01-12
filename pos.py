import pyautogui

while True:
    # Get the current position of the cursor
    cursor_x, cursor_y = pyautogui.position()

    print("Cursor position: ({}, {})".format(cursor_x, cursor_y))
