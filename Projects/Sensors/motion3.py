#Importing the GPIO library
import RPi.GPIO as GPIO

#Import time library
import time

#Set GPIO in pin mode: name pins by names with BCM
GPIO.setmode(GPIO.BCM)

#Set warnings not shown
GPIO.setwarnings(False)

pirpin = 23
buzpin = 27

#Setting pin 23 as the pin that inputs the signal from the PIR motion sensor to the Rasbpberry Pi
GPIO.setup(pirpin, GPIO.IN)

#Setting pin 27 as the pin that outputs the electricity from the Raspberry Pi to the Buzzer.
GPIO.setup(buzpin, GPIO.OUT)

print("Motion sensor alarm. Ctrl+c to exit")
time.sleep(2)
print("Ready")

try:
    while True:
        detect = GPIO.input(soundpin)
        if detect == 0:
            print("No motion detected")
            GPIO.output(buzpin, GPIO.LOW)
            time.sleep(2)
        else:
            print("Motioin detected")
            GPIO.output(buzpin, GPIO.HIGH)
            time.sleep(2)
except:
    print("Quit")
    GPIO.cleanup()
