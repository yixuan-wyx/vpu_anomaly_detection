import serial
import time
from datetime import datetime
import wave


'''
Read bin
'''
def get_filename(index):
    directory = "./output/Feather/bin/"
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    return f"{directory}audio_clip_{index}_{timestamp}.bin"

serial_port = '/dev/tty.usbmodem101' #MB_pro left_1
baud_rate = 500000  # Match the baud rate set on your Feather board


try:
    with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
        for i in range(6):
            # Open a new file for each audio clip
            filename = get_filename(i)
            with open(filename, "wb") as file:
                start_time = time.time()
                while time.time() - start_time < 5:  # Capture for 5 seconds
                    if ser.in_waiting:
                        data = ser.read(ser.in_waiting)
                        file.write(data)
            print(f"Captured and saved audio clip {i+1} to {filename}")
            # Optional: Delay between captures if needed
            time.sleep(1)
except serial.SerialException as e:
    print(f"Serial error: {e}")