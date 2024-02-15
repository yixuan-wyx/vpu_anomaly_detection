from scipy.fft import fft, ifft
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import librosa
import sklearn


audio = './output_data/knock/recording_knock_20240205_235543.wav'
fq, data = wavfile.read(audio)
# print(f'frequency:{fq}')

# plt.plot(data)
# plt.ylabel('Amplitude')
# plt.title("Example Audio")

fft_out = fft(data)
plt.plot(data, np.abs(fft_out))
plt.show()

# viz audio
# https://learnpython.com/blog/plot-waveform-in-python/
# plt.figure(figsize=(15, 5))
# plt.specgram(l_channel, Fs=sample_freq, vmin=-20, vmax=50)
# plt.title('Left Channel')
# plt.ylabel('Frequency (Hz)')
# plt.xlabel('Time (s)')
# plt.xlim(0, t_audio)
# plt.colorbar()
# plt.show()

# preprocessing
# https://medium.com/aiskunks/pre-processing-of-audio-data-e99718830e67
# https://www.altexsoft.com/blog/audio-analysis/
# https://www.comet.com/site/blog/working-with-audio-data-for-machine-learning-in-
# https://www.topcoder.com/thrive/articles/audio-data-analysis-using-python 


