#import necessary libraries
import time
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
from signal import pause
from gpiozero import LED, Buzzer, Button, MotionSensor

# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2

# Initialize I2C bus 
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

#RPi pin configuration
buzzer = Buzzer(6)
button = Button(13)
led = LED(5)
pir = MotionSensor(17)

#control variables
motion_sensor_status = False
lcd.clear()
lcd.color = [0, 50, 50]
led.off()

#arm or disarm the PIR sensor
def arm_motion_sensor():
    global motion_sensor_status
    if motion_sensor_status == True:
        motion_sensor_status = False
        led.off()
        buzzer.off()
        lcd.clear()
        lcd.color = [0, 50, 50]
        lcd.message = 'Alarm is off'
    else:
        motion_sensor_status = True
        lcd.clear()
        lcd.color = [0, 0, 100]
        lcd.message = 'Alarm is on'
        
#motion detected response
def motion_detected():
    global motion_sensor_status
    if (motion_sensor_status == True):
        if(pir.motion_detected):
            lcd.clear()
            lcd.color = [100, 0, 0]
            lcd.message = 'Alarm is on\nMotion detected!'
            led.blink()
            buzzer.blink()
        else:
            lcd.clear()
            lcd.color = [0, 0, 100]
            lcd.message = 'Alarm is on'
            led.off()
            buzzer.off()

button.when_pressed = arm_motion_sensor
pir.when_motion = motion_detected
pir.when_no_motion = motion_detected

#keep running to continuously check the pushbutton and pir states
pause()
            
