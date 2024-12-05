from pyautogui import *
from  time import sleep
from keyboard import *
sleep(3) # wait 3 seconds to close from app and determine the page
s=230    # Y-axis of The source's locationlocation
# where a copy is wanted
d=235   # Y-axis of The Destination's location where a copy is wanted
for i in range(4): #Loop to exec this operation 15 times
    moveTo(505, s,2) #over 2 seconds and move to the source location(Excel sheet)
    tripleClick()   # enter triple click on sheet
    moveTo(376, 176, 1) # over second go to sheet bar of Excel
    doubleClick()
    # Simulate Ctrl + C (copy)
    hotkey('ctrl', 'c')
    sleep(1)  # Wait for 1 second
    # Move to Destination (CM) over second and click
    moveTo(1172, d, 1)
    doubleClick()
    sleep(1)  # Wait for 1 second

    # Simulate Ctrl + V (paste)
    hotkey('ctrl', 'v')
    press('enter')
    sleep(1)
    write('3')
    press('enter')
    # Update coordinates for the next iteration
    s+=22
    d+=18






