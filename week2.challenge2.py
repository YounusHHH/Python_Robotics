from vexcode import *

# Add project code in "main"
def main():
    drivetrain.set_drive_velocity(30,PERCENT)
    drivetrain.drive(FORWARD)
    monitor_sensor("left_bumper.pressed","right_bumper.pressed") 
    while not left_bumper.pressed():
        wait(5, MSEC)
    drivetrain.stop()
    stop_project()

# VR threads — Do not delete
vr_thread(main())
