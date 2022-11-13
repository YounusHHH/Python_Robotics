from vexcode import *

def getLineBrightness(lineCounter,bright):
   brain.print(f"Brightness of {lineCounter}. Line: {bright}")
   brain.new_line()

def avgLineBrightness():
   global bright
   global brightnesses
   global lineCounter
   global total
   global avg
    
   
   total = 0
   avg = float(0)
   brightnesses = []
   
   drivetrain.set_drive_velocity(100,PERCENT)
   drivetrain.drive(FORWARD)
 
   while not left_bumper.pressed():
       wait(5, MSEC)
       if down_eye.brightness(PERCENT) < 100:
           bright = float(down_eye.brightness(PERCENT))
           brightnesses.append(bright)
           lineCounter = len(brightnesses)
           getLineBrightness(lineCounter,bright)
       while not down_eye.brightness(PERCENT) == 100:
           wait(5,MSEC)
   drivetrain.stop()
   for x in brightnesses:
       total += x
   avg = total / lineCounter
   brain.print("Average of Lines Brightness: ","{:.4f}".format(avg))
 
def main():
 
   avgLineBrightness()
 
   stop_project()
 
vr_thread(main())



How to avoid ZeroDivisionError?

If lineCounter doesn’t increase itself, program will be failed. So we must be careful about that.
