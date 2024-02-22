Helldivers 2 Queue Alert System

This repository contains a set of Python scripts designed to assist players of Helldivers 2 by automating the monitoring of queue status through screen region color analysis and providing an alert when you go through the queue.
Scripts Overview

    color average.py: Monitors a specified screen region and calculates the average color, continuously printing these values to the console. Useful for identifying the right screen region and color values to monitor for queue status.

    MouseX&Y.py: A utility script that displays the current mouse position in real-time. Helps in determining the coordinates of the screen region to be monitored.

    Queue alert system.py: The main script that monitors a specified screen region for color changes indicating a change in queue status. If the expected color is not detected within a defined tolerance for a certain period, it triggers an alert by setting the system volume to 100%, opening a predefined URL, and simulating a keypress.

Installation

To run these scripts, you'll need Python installed on your system along with several dependencies:

pip install pyautogui numpy Pillow pycaw webbrowser

Usage

    Setting Up: Use the MouseX&Y.py script to determine the screen region you wish to monitor. Note down the X, Y coordinates.

    Color Calibration: Run color average.py with the region of interest to find the average color you expect to monitor.

    Queue Monitoring: Update Queue alert system.py with the region, expected color, and tolerance. Run the script to start monitoring. Customize the alert actions as needed.

Customization

    Modify the screen region coordinates and dimensions in each script as needed.
    Adjust the expected color and tolerance in Queue alert system.py based on your calibration results.
    Change the URL in the alert action to any video or alert sound of your choice.

Disclaimer

This project is intended for educational purposes and personal use. Please respect the terms of service of any game or software you use it with.  The scripts and this readme were developed with ChatGPT.
