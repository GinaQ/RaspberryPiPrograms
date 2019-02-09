#import necessary libraries
import Adafruit_CharLCD as LCD
import time
from gpiozero import LED, Buzzer, Button, MotionSensor
from signal import pause

#RPi pin configuration
buzzer = Buzzer(6)
button = Button(13)
led = LED(5)
pir = MotionSensor(17)

#LCD
lcd_rs = 27   #register selection
lcd_en = 22   #enable
lcd_d4 = 25   #data pins
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18

#set the backlight level
lcd_backlight = 4

#define the lcd size
lcd_columns = 16
lcd_rows = 2

#initialize the LCD
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

#control variables
motion_sensor_status = False
lcd.clear()
led.off()

#arm or disarm the PIR sensor
def arm_motion_sensor():
    global motion_sensor_status
    if motion_sensor_status == True:
        motion_sensor_status = False
        led.off()
        buzzer.off()
        lcd.clear()
        lcd.message('Alarm is off')
    else:
        motion_sensor_status = True
        lcd.clear()
        lcd.message('Alarm is on')
        
#motion detected response
def motion_detected():
    global motion_sensor_status
    if (motion_sensor_status == True):
        if(pir.motion_detected):
            lcd.clear()
            lcd.message('Alarm is on\nMotion detected!')
            led.blink()
            buzzer.blink()
        else:
            lcd.clear()
            lcd.message('Alarm is on')
            led.off()
            buzzer.off()

button.when_pressed = arm_motion_sensor
pir.when_motion = motion_detected
pir.when_no_motion = motion_detected

#keep running to continuously check the pushbutton and pir states
pause()
            
