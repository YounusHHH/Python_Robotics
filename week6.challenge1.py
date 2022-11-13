# ------------------------------------------
# 
#   Project:      VEXcode Project
#   Author:       VEX
#   Created:
#   Description:  VEXcode VR Python Project
# 
# ------------------------------------------

# Library imports
from vexcode import *
def colorDict(brightness):
        switcher={
            58.7: "GREEN",
            11.4: "BLUE",
            29.9: "RED",
            100:"NONE",
        }
        return switcher.get(brightness,"corresponding color")
        
def blue():
    global current_brightness
    current_brightness=0
    global color
    color = "a"
    s = 0
    while not s==3:
        current_brightness=down_eye.brightness(PERCENT)
        color = colorDict(current_brightness)
        if  color == "BLUE":
            drivetrain.stop()
            magnet.energize(BOOST)
            drivetrain.turn_for(RIGHT, 180, DEGREES)
            while not right_bumper.pressed():
                drivetrain.drive(FORWARD)
                wait(5, MSEC)
            drivetrain.drive_for(REVERSE,200,MM)
            magnet.energize(DROP)
            drivetrain.turn_for(RIGHT, 180, DEGREES)
            s=s+1  
        elif color=="NONE":
            drivetrain.drive(FORWARD)  
        else:
            break
        wait(5,MSEC)

def red():
    global current_brightness
    current_brightness=0
    global color
    color = "a"
    s = 0
    while not s==3:
        current_brightness=down_eye.brightness(PERCENT)
        color = colorDict(current_brightness)
        if  color == "RED":
            drivetrain.stop()
            magnet.energize(BOOST)
            drivetrain.turn_for(RIGHT, 180, DEGREES)
            while not right_bumper.pressed():
                drivetrain.drive(FORWARD)
                wait(5, MSEC)
            drivetrain.drive_for(REVERSE,200,MM)
            magnet.energize(DROP)
            drivetrain.turn_for(RIGHT, 180, DEGREES)
            s=s+1    
        elif color=="NONE":
            drivetrain.drive(FORWARD)   
        else:
            break
        wait(5,MSEC)

def green():
    global current_brightness
    current_brightness=0
    global color
    color = "a"
    s = 0
    while not s==3:
        current_brightness=down_eye.brightness(PERCENT)
        color = colorDict(current_brightness)
        if  color == "GREEN":
            drivetrain.stop()
            magnet.energize(BOOST)
            drivetrain.turn_for(RIGHT, 180, DEGREES)
            while not right_bumper.pressed():
                drivetrain.drive(FORWARD)
                wait(5, MSEC)
            drivetrain.drive_for(REVERSE,200,MM)
            magnet.energize(DROP)
            drivetrain.turn_for(RIGHT, 180, DEGREES)
            s=s+1
        elif color=="NONE":
            drivetrain.drive(FORWARD)  
        else:
            break
        
        wait(5,MSEC) 
def Turn():
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 790, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)                    
# Add project code in "main"
def main():
    drivetrain.set_drive_velocity(100, PERCENT)
    monitor_variable("color","current_brightness")
    blue()
    Turn()
    red()
    Turn()
    green()
    stop_project()
# VR threads — Do not delete
vr_thread(main())



