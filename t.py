import cv2
import pyautogui
import numpy as np

def check_image_on_screen(image_path, button_position):
    # Load the images
    image = cv2.imread(image_path)
    screen = pyautogui.screenshot(region=(1238, 171, 195, 68))  # Specify the region of interest
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)

    # Get the width and height of the screen
    screen_width, screen_height = pyautogui.size()

    # Search for the image on the screen
    result = cv2.matchTemplate(screen, image, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= 0.8)  # Define the threshold for matching

    # Iterate through the found locations and perform the button press
    for loc in zip(*locations[::-1]):
        print("Image found at location:", loc)

        # Perform the button press at the specified position
        click_x, click_y = button_position
        screen_x = int(click_x * screen_width / 1920)  # Adjust for screen resolution (1920x1080)
        screen_y = int(click_y * screen_height / 1080)  # Adjust for screen resolution (1920x1080)
        pyautogui.click(x=screen_x, y=screen_y)

# Specify the file paths for the images
image1_path = "image1.png"
image2_path = "image2.png"

# Specify the position of the button (absolute coordinates relative to 1920x1080 resolution)
button_position = (1440, 940)  # Change the coordinates as per your requirement

while True:
    # Check if image1 is on the screen and click the button if found
    check_image_on_screen(image1_path, button_position)

    # Check if image2 is on the screen and click the button if found
    check_image_on_screen(image2_path, button_position)
