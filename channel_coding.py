from util import *
import numpy as np

G = [[1, 1, 0, 1],
     [1, 0, 1, 1],
     [1, 0, 0, 0],
     [0, 1, 1, 1],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]

def channelCoding():
    print("QUESTION 8:")
    printWav()
    print("QUESTION 9:")


def convert_binary(signal):
    bin_signal = []
    for value in signal:
        bin_signal.append([int(x) for x in '{0:08b}'.format(value)])
    return np.array(bin_signal)

def encode(bin_signal):
    code = np.zeros((len(bin_signal), 14))
    for i in range(len(bin_signal)):
        code[i][:7] = hamming(bin_signal[i][:4])
        code[i][7:] = hamming(bin_signal[i][4:])
    return code

def hamming(bin_signal):
    return np.mod(np.dot(G, bin_signal), 2)

if __name__ == "__main__":
    code = encode(convert_binary(read("sound.wav")[1]))
    print(code[0])
    print(np.shape(code))
