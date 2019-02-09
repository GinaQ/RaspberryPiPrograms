#import necessary libraries
from gpiozero import LED, Button
from signal import pause
from time import sleep

#set GPIO pins
led = LED(18)
button = Button(2)


led_on = led.is_active
if (led_on):
    button.when_pressed = led.off
    button.when_released = sleep(1)
if (led_on == False):
    button.when_pressed = led.off
    button.when_released = sleep(1)
else:
    led.on

#keep running to continuously check the pushbutton state
pause()

