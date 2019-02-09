#Importing the GPIO library
import RPi.GPIO as GPIO

#Import time library
import time

#Set GPIO in pin mode: name pins by names with BCM
GPIO.setmode(GPIO.BCM)

#Set warnings not shown
GPIO.setwarnings(False)

#Setting pin 17 as the pin that inputs the signal from the PIR motion sensor to the Rasbpberry Pi
GPIO.setup(17, GPIO.IN)

#Setting pin 2 as the pin that outputs the electricity from the Raspberry Pi to the Buzzer.
GPIO.setup(2, GPIO.OUT)

#Begin while loop
while True:
    detect = GPIO.input(17)
    #Sound buzzer based on value of detect (1 for true, 0 for false)
    if detect == 0:
        print("No motion detected")
        GPIO.output(2, GPIO.LOW)
        time.sleep(2)
    else:
        print("Motion detected")
        GPIO.output(2, GPIO.HIGH)
        time.sleep(2)
        
