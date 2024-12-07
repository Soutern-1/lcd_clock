#! /usr/bin/env python
import time

import drivers
from time import sleep

display = drivers.Lcd()


cc = drivers.CustomCharacters(display)

time_object = time.localtime()
local_time = time.strftime("%H:%M:%S", time_object)

line1 = ""
line2 = ""



# Redefine the default characters:
# Custom caracter #1. Code {0x00}.
cc.char_1_data = ["00001",
                  "00001",
                  "00001",
                  "00001",
                  "00001",
                  "00001",
                  "00001",
                  "00001"]

# Custom caracter #2. Code {0x01}.
cc.char_2_data = ["11111",
                  "00001",
                  "00001",
                  "00001",
                  "00001",
                  "00001",
                  "10001",
                  "11111"]

# Custom caracter #3. Code {0x02}.
cc.char_3_data = ["11111",
                  "00001",
                  "00001",
                  "00001",
                  "00001",
                  "00001",
                  "00001",
                  "00001"]

# Custom caracter #4. Code {0x03}.
cc.char_4_data = ["10000",
                  "10000",
                  "10000",
                  "10000",
                  "10000",
                  "10001",
                  "10001",
                  "11111"]

# Custom caracter #5. Code {0x04}.
cc.char_5_data = ["11111",
                  "10000",
                  "10000",
                  "10000",
                  "10000",
                  "10000",
                  "10000",
                  "10000"]

# Custom caracter #6. Code {0x05}.
cc.char_6_data = ["11111",
                  "10001",
                  "10001",
                  "10001",
                  "10001",
                  "10001",
                  "10001",
                  "11111"]

# Custom caracter #7. Code {0x06}.
cc.char_7_data = ["11111",
                  "10001",
                  "10001",
                  "10001",
                  "10001",
                  "10001",
                  "10001",
                  "10001"]

# Custom caracter #8. Code {0x07}.
cc.char_8_data = ["10001",
                  "10001",
                  "10001",
                  "10001",
                  "10001",
                  "10001",
                  "10001",
                  "11111"]
# Load custom characters  to CG RAM:
cc.load_custom_characters_data()

def create_lines():
    global local_time, line1, line2
    for i in local_time:
        if i == 1:
            line1 +="{0x00}"
            line2 +="{0x00}"
        if i == 2:
            line1 +="{0x01}"
            line2 +="{0x03}"
        if i ==3:
            line1+="{0x01}"
            line2+="{0x01}"
        if i ==4:
            line1+="{0x03}"
            line2+="{0x00}"
        if i ==5:
            line1+="{0x04}"
            line2+="{0x01}"
        if i ==6:
            line1+="{0x00}"
            line2+="{0x05}"
        if i ==7:
            line1+="{0x04}"
            line2+="{0x00}"
        if i ==8:
            line1+="{0x06}"
            line2+="{0x05}"
            
        if i ==9:
            line1+="{0x05}"
            line2+="{0x00}"
        if i ==0:
            line1+= "{0x06}"
            line2+= "{0x07}"
        if i == ":":
            line1+="  "
            line2+="  "
    

# Main body of code
try:
    while True:


        print("Printing custom characters:")
        create_lines()
        display.lcd_display_extended_string(line1, 1)  # Write 1st line of text to first line of display
        display.lcd_display_extended_string(line2, 2)  # Write 2nd line of text to second line of display
        sleep(1) # Refresh evey 1 second
except KeyboardInterrupt:
    
    print("Cleaning up!")
    display.lcd_clear()