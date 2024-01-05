# Warning! This script will automatically control cursor movement.

import pyautogui
import time

#print(pyautogui.size())
# 1920*1080

time.sleep(4)
# Delay Time For Changing Windows to Your Browser Before Starting Scroll Loop

pyautogui.moveTo(500,900,duration=1)
# Move Cursor to Select 'More Results' Button

for i in range(300):
    time.sleep(0.5)
    pyautogui.click(500,900,duration=1)
    pyautogui.scroll(-2000)
# Click Button and Scroll Automatically, Exit with Ctrl-c.

# When complete, Select All Google Result and Copy, Then, open text editor, paste the copied content, and make sure to remove personal data (your location in the footer).
