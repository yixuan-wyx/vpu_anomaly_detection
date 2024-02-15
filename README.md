# vpu_anomaly_detection

# Overall Flow:

- Task: collecting raw PCM audio data from a VPU sensor connected to an Adafruit Feather M0 Express board, converting it to WAV format, and then analyzing it.

- Functions of each script:
1. code.py (On the Adafruit Feather M0 Express)
**Purpose**: Continuously captures audio data from the VPU sensor and sends it over the serial connection to your computer. This script runs directly on the Feather board.
**Action**: Initializes the microphone (VPU sensor), captures audio data in real-time, and streams this data over the serial port to be read by your computer.

```
**Raw PCM output:**

# Initialize microphone with a 20 kHz sample rate
mic = audiobusio.PDMIn(board.SCK, board.D9, sample_rate=20000, bit_depth=16) # 16000, 20000

# Define a smaller buffer for continuous capture and transmission
buffer_size = 512  # A smaller buffer for continuous processing
audio_buffer = bytearray(buffer_size)

while True:
    mic.record(audio_buffer, len(audio_buffer))
    # Stream each buffer's worth of audio data over serial
    print(audio_buffer, end = '')
    # Optional: Adjust based on the capability of your serial communication
    time.sleep(0.01)  # A short sleep to prevent overwhelming the serial port
```

2. read_serial.py (On Your Local Computer)
**Purpose**: Receives the raw PCM audio data streamed over the serial connection from the Feather board and saves this data into .bin files on your computer. Each file represents a segment of captured audio data (e.g., 5 seconds).
**Action**: Opens the serial port, reads incoming audio data for predefined intervals (e.g., 5 seconds), saves each interval as a .bin file, and repeats this process for the desired number of audio clips.
Terminal command:
```
python read_serial.py
```

3. convert_to_wav.py (On Your Local Computer)
**Purpose**: Converts the raw PCM audio data files (.bin) saved by read_serial.py into standard WAV format files that can be easily used for further analysis or playback.
**Action**: Reads each .bin file, adds appropriate WAV headers (including sample rate, bit depth, and channels information), and saves the result as a .wav file.
Terminal command:
```
python convert_to_wav.py
```

# Execution Order:
First, ensure code.py is correctly placed on your Feather board and the board is operational, capturing and sending audio data over serial. Add the code.py file to CIRCUITPY Drive


Second, run read_serial.py on your local computer to start receiving the audio data from your Feather board. This script should be kept running as long as you want to capture audio data. It will automatically segment the audio into chunks and save them as .bin files.


Lastly, after you've captured all desired audio data, run convert_to_wav.py for each of the .bin files to convert them into .wav files for further analysis or processing.

