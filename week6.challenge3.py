
from vexcode import *
def colorDict(brightness):
        switcher={
            58.7: "GREEN",
            11.4: "BLUE",
            29.9: "RED",
            100:"NONE",
        }
        return switcher.get(brightness,"corresponding color")
# Add project code in "main"
def main():
    global current_brightness
    current_brightness=0
    global color
    color = "a"
    monitor_variable("color","current_brightness")
    drivetrain.drive(FORWARD)
    x = 0
    for x in range(2):
        while 1:
            current_brightness=down_eye.brightness(PERCENT)
            color = colorDict(current_brightness)
            if color == "GREEN":
                drivetrain.turn_for(RIGHT, 90,DEGREES)
                brain.print(colorDict(current_brightness))
                brain.new_line()
            elif color == "BLUE":
                drivetrain.turn_for(LEFT,90,DEGREES)
                brain.print(colorDict(current_brightness))
                brain.new_line()
            elif color=="RED":
                brain.print(colorDict(current_brightness))
                brain.new_line()
                drivetrain.turn_for(RIGHT,90,DEGREES)
                drivetrain.drive_for(FORWARD,1250,MM)
                drivetrain.turn_for(RIGHT,90,DEGREES)
                break
            else:
                drivetrain.drive(FORWARD)
                
            wait(5,MSEC)
            x= x+1
        wait(5,MSEC)
    stop_project()
# VR threads — Do not delete
vr_thread(main())


