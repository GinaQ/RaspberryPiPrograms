import RPi.GPIO as GPIO
import time

#set GPIO pin mode: name pins by names with BCM
GPIO.setmode(GPIO.BCM)

#set warnings not shown
GPIO.setwarnings(False)

redPin = 17
greenPin = 27
bluePin = 22

def turnOn(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.5)

def turnOff(pin):
    GPIO.output(pin, GPIO.LOW)

def whiteOn():
    turnOn(redPin)
    turnOn(bluePin)
    turnOn(greenPin)
    time.sleep(0.5)

def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)

def ledShow():
    max_count = 2
    count = 0
    while(count <= max_count):
        turnOn(redPin)
        turnOff(redPin)
        turnOn(greenPin)
        turnOff(greenPin)
        turnOn(bluePin)
        turnOff(bluePin)
        whiteOn()
        whiteOff()
        count = count + 1

cmd = input("Start the LED show: (y/n)")

if cmd == "y":
    ledShow()
else:
    quit()
