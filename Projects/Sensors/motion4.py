import RPi.GPIO as GPIO
import time

#Set GPIO in pin mode: name pins by names with BCM
GPIO.setmode(GPIO.BCM)

#Set warnings not shown
GPIO.setwarnings(False)

pirpin = 17
buzpin = 27

#Setting pin 17 as the pin that inputs the signal from the PIR motion sensor to the Rasbpberry Pi
GPIO.setup(pirpin, GPIO.IN)

#Setting pin 2 as the pin that outputs the electricity from the Raspberry Pi to the Buzzer.
GPIO.setup(buzpin, GPIO.OUT)

def BUZZ(pirpin):
    #Turn buzzer on and off
    print("Motion detected")
    print("Buzzer on")
    GPIO.output(buzpin, GPIO.HIGH)

    time.sleep(2)

    print("Buzzer off")
    GPIO.output(buzpin, GPIO.LOW)
    

print("Motion sensor alarm. Ctrl+c to exit")
time.sleep(2)
print("Ready")

try:
    #Add event listener
    GPIO.add_event_detect(pirpin, GPIO.RISING, callback=BUZZ)
    #Begin while loop
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()

    
