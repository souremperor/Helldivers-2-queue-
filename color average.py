import pyautogui
from PIL import Image
import numpy as np

def capture_screen_region(x, y, width, height):
    # Capture a specific region of the screen
    image = pyautogui.screenshot(region=(x, y, width, height))
    return image

def calculate_average_color(image):
    # Convert the captured image to a NumPy array
    np_image = np.array(image)
    # Calculate the average color (across all pixels and for each RGB channel)
    avg_color = np.mean(np_image.reshape(-1, np_image.shape[2]), axis=0)
    return avg_color

# Define the region of the screen you want to monitor (x, y, width, height)
# Using the coordinates and dimensions you provided
region = (1320, 796, 19, 25)

while True:
    # Capture the screen region
    screen_capture = capture_screen_region(*region)
    
    # Calculate the average color of the captured region
    avg_color = calculate_average_color(screen_capture)
    
    # Print the average color in RGB format
    print(f"Average Color: {avg_color}")

    # Pause for a bit before checking again to avoid overwhelming your CPU
    pyautogui.sleep(1)

