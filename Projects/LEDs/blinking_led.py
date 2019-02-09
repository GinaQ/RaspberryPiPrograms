#importing necessary libraries
from gpiozero import LED
from time import sleep

#create an object called led that refers to GPIO 25
led_red = LED(25)
led_blue = LED(23)
led_yellow = LED(24)

#create a variable called delay that refers to delay time in seconds
delay = 1

while True:
    #set led to on for the delay time
    led_red.on()
    #print('LED set to on')
    sleep(delay)
    #set led to off for the delay time
    led_red.off()
    #print('LED set to off')
    #sleep(delay)
    led_blue.on()
    sleep(delay)
    led_blue.off()
    led_yellow.on()
    sleep(delay)
    led_yellow.off()
    led_red.on()
    led_blue.on()
    led_yellow.on()
    sleep(delay)
    led_red.off()
    led_blue.off()
    led_yellow.off()
    sleep(delay)
    
