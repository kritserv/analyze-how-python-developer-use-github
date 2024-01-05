# Warning! This script will automatically control mouse and keyboard movement.

import pyautogui
import time

#print(pyautogui.size())
# 1920*1080

time.sleep(4)
# Time For Changing Windows to Your Browser Before Start

pyautogui.moveTo(500,900,duration=1)
# Move Cursor to Select 'More Results' Button

for i in range(300):
    time.sleep(0.5)
    pyautogui.click(500,900,duration=1)
    pyautogui.scroll(-1500)
# Click Button and Scroll Automatically, Exit with Ctrl-c.

# When complete, Select All and Copy, Then, open text editor, paste the copied result, and make sure to remove personal data (your location in the footer).
