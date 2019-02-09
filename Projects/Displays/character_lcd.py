#import necessary libraries
import Adafruit_CharLCD as LCD

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
lcd.show_cursor(True)
lcd.message('It works\nYou rock!')
