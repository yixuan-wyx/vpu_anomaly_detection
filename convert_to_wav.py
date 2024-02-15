import wave
import os

def convert_bin_to_wav(bin_file_path, wav_file_path, channels=1, sampwidth=2, framerate=20000):

    """
    Convert a .bin file with raw PCM audio into a .wav file.

    Parameters:
    - bin_file_path: Path to the input .bin file.
    - wav_file_path: Path to the output .wav file.
    - channels: Number of audio channels (1 for mono, 2 for stereo).
    - sampwidth: Sample width in bytes (2 for 16-bit audio).
    - framerate: Sample rate of the audio (e.g., 20000 for 20 kHz).
    """
     
    with open(bin_file_path, 'rb') as bin_file:
        raw_data = bin_file.read()

    with wave.open(wav_file_path, 'w') as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(sampwidth)
        wav_file.setframerate(framerate)
        wav_file.writeframes(raw_data)


bin_dir = './output/Feather/bin/'
wav_dir = './output/Feather/wav/'

files = [f for f in os.listdir(bin_dir) if f.endswith('.bin')]

for file in files:
    bin_file_path = os.path.join(bin_dir, file)
    wav_file_path = os.path.join(wav_dir, file.replace('.bin', '.wav'))
    convert_bin_to_wav(bin_file_path, wav_file_path)
