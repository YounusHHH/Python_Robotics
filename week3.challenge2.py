
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
    while True:
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
        elif color== "NONE":
            drivetrain.drive(FORWARD)
        elif color=="RED":
            break
        wait(5,MSEC)
    stop_project()
# VR threads — Do not delete
vr_thread(main())


