#import necessary libraries
import Adafruit_CharLCD as LCD
import time

#Raspberry Pi pin configuration
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

#display message
title = "Don't forget!"
reminder = "You have a doctor appointment next Monday"

#set the delay for scroll
delay = 0.3

#write a function to scroll the message
def scroll_message(reminder, delay):
    padding = ' ' * lcd_columns
    reminder_message = padding + reminder + ' '
    for i in range(len(reminder_message)):
        lcd.set_cursor(0,1)
        lcd.message(reminder_message[i:(i+lcd_columns)])
        time.sleep(delay)

lcd.clear()
lcd.home()
lcd.message(title)

#scroll the message in an infinite loop
while True:
    scroll_message(reminder, delay)
