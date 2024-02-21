import pyautogui
import time

try:
    while True:
        # Get the current mouse x and y positions
        x, y = pyautogui.position()
        # Print these positions
        print(f"X: {x} Y: {y}", end='\r')
        time.sleep(1)  # Pause for 1 second to make it readable
except KeyboardInterrupt:
    print("\nDone")  # When you press CTRL+C to stop the script, it will print "Done"

