import pyautogui
from PIL import Image
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import webbrowser
import time  # Import time module

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

def color_distance(color1, color2):
    # Calculate the Euclidean distance between two colors
    return np.sqrt(np.sum((color1 - color2) ** 2))

def set_volume(percent):
    # Convert the volume setting from percentage to a scalar between 0.0 and 1.0
    volume_level = percent / 100.0
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level, None)

def play_video(url):
    # Use the webbrowser module to open the provided URL in the default browser
    webbrowser.open(url)
    time.sleep(10)  # Wait for 10 seconds after opening the video
    pyautogui.press('space')  # Simulate pressing the space bar

# Define the region of the screen you want to monitor (x, y, width, height)
region = (1320, 796, 19, 25)

# Expected color
expected_color = np.array([190.29, 189.97, 162.90])

# Tolerance for color matching
tolerance = 10

# Counter for consecutive non-matches
non_match_count = 0

while True:
    # Capture the screen region
    screen_capture = capture_screen_region(*region)
    
    # Calculate the average color of the captured region
    avg_color = calculate_average_color(screen_capture)
    
    # Check if the detected color matches the expected color within the tolerance
    if color_distance(avg_color, expected_color) > tolerance:
        non_match_count += 1
        print(f"Color does not match. Count: {non_match_count}")
        if non_match_count >= 120:
            print("Alert: Color has not matched 10 times in a row!")
            # Set volume to 100%
            set_volume(100)  # Adjusted to set the volume to 100 percent
            # Play the video and wait 10 seconds before pressing space
            play_video("https://youtu.be/dQw4w9WgXcQ")
            break  # Stop the script or reset non_match_count if you want to continue monitoring
    else:
        non_match_count = 0  # Reset counter if a match is found
    
    # Pause for a bit before checking again
    pyautogui.sleep(1)

