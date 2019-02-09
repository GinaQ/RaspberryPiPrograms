import time
from gpiozero import MotionSensor

pir = MotionSensor(17)

while True:
    if (pir.motion_detected == True):
        print("motion detected")
        time.sleep(1)
    else:
        print("no motion detected")
        time.sleep(1)


