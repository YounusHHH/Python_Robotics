
from vexcode import *

# Add project code in "main"
def main():
    
    drivetrain.drive(FORWARD)
    monitor_sensor("down_eye.brightness") 
    while not down_eye.brightness(PERCENT)==29.9:
        wait(5, MSEC)
    drivetrain.stop()
    stop_project()

# VR threads — Do not delete
vr_thread(main())



# ------------------------------------------

from vexcode import *

# Add project code in "main"
def main():
    
    drivetrain.drive(FORWARD)
    monitor_sensor("down_eye.brightness") 
    while not 28< down_eye.brightness(PERCENT)<30:
        wait(5, MSEC)
    drivetrain.stop()
    stop_project()

# VR threads — Do not delete
vr_thread(main())
