
import serial
import keyboard
import time
from datetime import datetime, timedelta

ser = serial.Serial('COM3', 115200)
is_left = False
is_right = False
key_pressed = False
new_key = False
next_send = datetime.now()
input_msg = ''

while True:
    if keyboard.is_pressed('left'):
        if is_left:
            next_send = datetime.now() + timedelta(milliseconds=200)
            is_right = False
        else:
            new_key = False
        print('L')
        input_msg = b"R\n"
        is_left = True
        is_right = False
        key_pressed = True

    if keyboard.is_pressed('right'):
        if is_right:
            next_send = datetime.now() + timedelta(milliseconds=200)
            is_left = False
        else:
            new_key = True
        print('R')
        input_msg = b"R\n"
        is_left = False
        is_right = True
        key_pressed = True

    if datetime.now() <= next_send and len(input_msg) > 0 and key_pressed:
        ser.write(input_msg)

    key_pressed = False
