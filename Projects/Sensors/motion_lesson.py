import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.OUT)

while True:
    detect = GPIO.input(17)
    if detect == 0:
        print("no motion detected")
        GPIO.output(27, GPIO.LOW)
        time.sleep(2)
    else:
        print ("motion detected")
        GPIO.output(27, GPIO.HIGH)
        time.sleep(2)
        
GPIO.cleanup()
