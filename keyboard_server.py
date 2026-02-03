
import serial
import keyboard
import time
from datetime import datetime, timedelta

new_key = False
next_send = datetime.now()
input_msg = ''

import serial
import time

with serial.Serial('COM3', 115200, timeout=0.1) as ser:
    while True:
        if keyboard.is_pressed('left'):
            print('<--Left')
            input_msg = b"L\n"

        elif keyboard.is_pressed('right'):
            print('Right-->')
            input_msg = b"R\n"

        else:
            print('None')
            input_msg = b"N\n"

        # Write only when you actually have something to send
        ser.write(b"Hello\n")
        
        # Micro-polling loop for receiving
        # This keeps the script responsive without high CPU usage
        start_time = time.time()
        while time.time() - start_time < 0.5: # Wait up to 0.5s for a reply
            if ser.in_waiting > 0:
                response = ser.readline().decode('utf-8').strip()
                print(f"Received: {response}")
                break # Exit micro-loop once data is found
            time.sleep(0.01) # Tiny sleep to free CPU

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
