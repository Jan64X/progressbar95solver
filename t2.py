import cv2
import pyautogui
import numpy as np
import datetime

def check_image_on_screen(image_path):
    global last_press_time

    # Load the image
    image = cv2.imread(image_path)
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)

    # Search for the image on the screen
    result = cv2.matchTemplate(screen, image, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= 0.8)  # Define the threshold for matching

    # Check if the minimum time has passed since the last press
    if (datetime.datetime.now() - last_press_time).total_seconds() >= 30:
        # Iterate through the found locations and simulate the press of the minus button
        for loc in zip(*locations[::-1]):
            print("Image found at location:", loc)
            pyautogui.press('o')
            last_press_time = datetime.datetime.now()
            break  # Exit the loop after the first press

# Specify the file paths for the images
image1_path = "image3.png"
image2_path = "image3.png"

last_press_time = datetime.datetime.now()

while True:
    # Check if image1 is on the screen and press the minus button if found
    check_image_on_screen(image1_path)

    # Check if image2 is on the screen and press the minus button if found
    check_image_on_screen(image2_path)
