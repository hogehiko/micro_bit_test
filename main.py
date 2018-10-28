# Add your Python code here. E.g.
from microbit import *

state = True
while True:
    reading = accelerometer.get_x()
    if reading > 0:
        if state != True:
            display.scroll("tenji", wait=False)
            state = True

    else:
        if state != False:
            display.scroll("anpanman", wait=False)
            state= False
    
    