from CST import *
import collections
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
import numpy as np
import wave
import sys


def write_wav(filename, sampling_rate, data):
    """
    Writing a .wav file from the data taken in input
    """
    data = np.asarray(data, dtype=np.int16)
    write(filename, sampling_rate, data)

def print_wav(filename, name):
    """
    Print the signal of the .wav sound.

    This code was made by the stackoverflow user CuriousCoder and can be found
    at : https://stackoverflow.com/questions/18625085/how-to-plot-a-wav-file/18625294
    """
    # read audio samples
    input_data = read(filename)
    audio = input_data[1]
    fig = plt.figure()
    # plot the first 1024 samples
    plt.plot(audio[0:-1])
    # label the axes
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    # set the title
    plt.title("Sample Wav")
    # display the plot
    fig.savefig(name+".png", dpi=300)


def printSortedDict(d):
    """
    Print the dict sorted by its items
    """
    od = collections.OrderedDict(sorted(d.items()))
    for key, value in od.items():
        if key == "\n":
            print("\"\\n\" : {}".format(value))
        else:
            print("\"{}\" : {}".format(key, value))


def lowestKeyDict(p):
    sorted_p = sorted(p.items(), key=lambda x: x[1])
    return sorted_p[0][0]
