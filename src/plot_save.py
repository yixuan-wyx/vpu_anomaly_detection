from time import sleep
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


fsamp = 16000                     # Sampling rate

# countdown
def countdown(t):
    print('You can start moving the object in:')
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        sleep(1)
        t -= 1
    print("Start moving the object now!")

# plot
def plotAll(surface_type, x):
    timestamp = datetime.now().strftime("%m%d_%H%M")
    
    plotname = f'output_data/{surface_type}/plot_{surface_type}_{timestamp}.png'
    runtime = 50  # 100   

    t = np.arange(len(x))/fsamp

    with plt.style.context(('dark_background')):
        fig, axs = plt.subplots(1, 1, figsize=(7, 2.5))
        lw,     = axs.plot(t, x, 'r')
        axs.grid(which='major', alpha=0.2)
        axs.set_xlim(0, t[-1])
        plt.tight_layout()
        # save the plot
        # plt.savefig('./plot.png')
        plt.savefig(plotname)
    return