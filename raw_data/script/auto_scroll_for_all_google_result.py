# Warning! This script will automatically control cursor movement.

import pyautogui
import time

#print(pyautogui.size())
# 1920*1080

# Before Running this Script Search Google with Specific Site for example:
# site:www.linkedin.com/in "github.com/" "python developer"

# Delay Time For Changing Windows to Your Browser Before Starting Scroll Loop
time.sleep(4)
pyautogui.moveTo(500,900,duration=1)

# Keep Scrolling to get 'More Results' Button
for i in range(6):
    time.sleep(0.7)
    pyautogui.scroll(-2000)
    time.sleep(0.7)

# Move Cursor to Select 'More Results' Button
pyautogui.moveTo(500,900,duration=1)

# Click Button and Scroll Automatically, Exit with Ctrl-c.
for i in range(300):
    time.sleep(0.7)
    pyautogui.click(500,900,duration=1)
    pyautogui.scroll(-2000)

# When complete, Select All Google Result and Copy, Then, open text editor, paste the copied content, and make sure to remove personal data (your location in the footer).
