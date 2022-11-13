from vexcode import *

def getLineBrightness(lineCounter,bright):
   brain.print(f"Brightness of {lineCounter}. Line: {bright}")
   brain.new_line()

def avgLineBrightness():
   global bright
   global lineCounter
   global total
   global avg
 
   total = 0
   lineCounter = 0
   avg = float(0)
 
   drivetrain.set_drive_velocity(100,PERCENT)
   drivetrain.drive(FORWARD)
 
   while not left_bumper.pressed():
       wait(5, MSEC)
       if down_eye.brightness(PERCENT) < 100:
           bright = float(down_eye.brightness(PERCENT))
           lineCounter += 1
           total += down_eye.brightness(PERCENT)
           getLineBrightness(lineCounter,bright)
       while not down_eye.brightness(PERCENT) == 100:
           wait(5,MSEC)
   drivetrain.stop()
   avg = total / lineCounter
   brain.print("Average of Lines Brightness: ","{:.4f}".format(avg))
 
def main():
 
   avgLineBrightness()
 
   stop_project()
 
vr_thread(main())
