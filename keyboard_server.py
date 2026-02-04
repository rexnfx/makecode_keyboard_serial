
import keyboard
import serial
import time

input_msg = ''

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
        ser.write(input_msg)
        
        # Micro-polling loop for receiving
        # This keeps the script responsive without high CPU usage
        start_time = time.time()
        while time.time() - start_time < 0.5: # Wait up to 0.5s for a reply
            if ser.in_waiting > 0:
                response = ser.readline().decode('utf-8').strip()
                print(f"Received: {response}")
                break # Exit micro-loop once data is found
            time.sleep(0.01) # Tiny sleep to free CPU

