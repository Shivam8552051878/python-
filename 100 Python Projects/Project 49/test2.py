import pyautogui
import time

# Wait for a few seconds to give you time to focus on the file selection dialog
time.sleep(5)

# Simulate a series of clicks and key presses to select a file
pyautogui.click(x=500, y=500)  # Click to focus on the file selection dialog

# Depending on the file dialog, you might need to adjust the coordinates and actions below.
pC:\glis-3000\Release\Captured Images\20230814154442_Mix.bmp
yautogui.typewrite("C:\\glis-3000\\Release\\Captured Images\\20230814154442_Mix.bmp")  # Type the path of the file
pyautogui.press("enter")  #