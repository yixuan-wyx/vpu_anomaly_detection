#!/usr/bin/python

import sys
import serial
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from scipy.io import wavfile
from datetime import datetime
from src.plot_save import countdown, plotAll


do_plot = True
do_save = True

# Audio Format & Datatype
dtype = np.int16                  # Data type to read data
typelen = np.dtype(dtype).itemsize  # Length of data type
maxval = 32768.  # 2**15            # For 16bit signed

# Plot Parameters
delay = .00001                    # Use 1us pauses - as in matlab
fsamp = 16000                     # Sampling rate
nframes = 10                        # No. of frames to read at a time
buflen = fsamp//10                 # Buffer length
bufsize = buflen*typelen            # Resulting number of bytes to read
window = fsamp*10                  # window of signal to plot at a time in samples


def main():
    surface_type = input("Enter the surface type: ")
    countdown(5)

    timestamp = datetime.now().strftime("%m%d_%H%M")
    wavname = f'output_data/{surface_type}/recording_{surface_type}_{timestamp}.wav'
    runtime = 50  # 100 

    sPort = "/dev/cu.usbmodem1101"
    ser = serial.Serial(sPort, 500000)
    ser.reset_input_buffer()
    ser.reset_output_buffer()

    x = [0]*window
    t = np.arange(window)/fsamp         # [x/fsamp for x in range(10)]

    plt.ion()
    plt.show()

    with plt.style.context(('dark_background')):
        fig, axs = plt.subplots(1, 1, figsize=(7, 2.5))
        lw, = axs.plot(t, x, 'r')
        axs.set_xlim(0, window/fsamp)
        axs.grid(which='major', alpha=0.2)
        axs.set_ylim(-1, 1)
        axs.set_xlabel('Time (s)')
        axs.set_ylabel('Amplitude')
        axs.set_title('Streaming Audio')
        plt.tight_layout()
        plt.pause(0.001)

    # Start Transmission
    ser.write('START'.encode())     # Send Start command
    sleep(1)

    for _ in range(runtime):
        buf = ser.read(bufsize)                 # Read audio data
        buf = np.frombuffer(buf, dtype=dtype)    # Convert to int16
        buf = buf/maxval                        # convert to float
        x.extend(buf)                           # Append to waveform array

        # Update Plot lines
        lw.set_ydata(x[-window:])

        plt.pause(0.001)
        sleep(delay)

    # Stop Streaming
    ser.write('STOP'.encode())
    sleep(0.5)
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    ser.close()

    # Remove initial zeros
    x = x[window:]

    if do_plot:
        plt.close(fig)
        plotAll(surface_type, x)

    # Save Recorded Audio
    if do_save:
        wavfile.write(wavname, fsamp, np.array(x))
        print(f"Recording saved to file: {wavname}")


if __name__ == '__main__':
    main()
