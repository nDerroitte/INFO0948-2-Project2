from util import *
import numpy as np


G = [[1, 1, 0, 1],
     [1, 0, 1, 1],
     [1, 0, 0, 0],
     [0, 1, 1, 1],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]

H = [[1, 0, 1, 0, 1, 0, 1],
     [0, 1, 1, 0, 0, 1, 1],
     [0, 0, 0, 1, 1, 1, 1]]

R = [[0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 1]]

def convert_binary(signal):
    bin_signal = []
    for value in signal:
        bin_signal.append([int(x) for x in '{0:08b}'.format(value)])
    return np.array(bin_signal)

def convert_int(bin_signal):
    signal = np.zeros(len(bin_signal), dtype=int)
    for i in range(len(bin_signal)):
        for bit in bin_signal[i]:
            signal[i] = (signal[i] << 1) | bit
    return signal

def encode_signal(bin_signal):
    coded_sig = np.zeros((len(bin_signal), 14), dtype=int)
    for i in range(len(bin_signal)):
        coded_sig[i][:7] = hamming(bin_signal[i][:4])
        coded_sig[i][7:] = hamming(bin_signal[i][4:])
    return coded_sig

def invert_bit(bit):
    if bit:
        bit = 0
    else:
        bit = 1
    return bit

def add_noise(signal):
    n_signal = signal.copy()
    for i in range(len(n_signal)):
        for j in range(len(n_signal[i])):
            if np.random.choice(2, 1, p=[0.99, 0.01]):
                n_signal[i][j] = invert_bit(n_signal[i][j])
    return n_signal

def check_coded_sig(coded_sig):
    syn_matrix = np.zeros((len(coded_sig), 6), dtype=int)
    for i in range(len(coded_sig)):
        syn_matrix[i][:3] = parity_check(coded_sig[i][:7])
        syn_matrix[i][3:] = parity_check(coded_sig[i][7:])
    return syn_matrix

def parity_check(code):
    return np.mod(np.dot(H, code), 2)

def decode_signal(coded_sig):
    bin_signal = np.zeros((len(coded_sig), 8), dtype=int)
    for i in range(len(coded_sig)):
        bin_signal[i][:4] = rev_hamming(coded_sig[i][:7])
        bin_signal[i][4:] = rev_hamming(coded_sig[i][7:])
    return bin_signal

def hamming(bin_value):
    return np.mod(np.dot(G, bin_value), 2)

def rev_hamming(code):
    return np.dot(R, code)

def channel_coding():
    print("QUESTION 8:")
    print_wav('sound.wav')
    print("QUESTION 9:")

if __name__ == "__main__":
    # load the signal from the file
    signal = read('sound.wav')[1]
    # display the original signal
    print_wav('sound.wav', "original sound")
    # convert the signal into a binary signal
    bin_signal = convert_binary(signal)
    # encode the binary signal using the hamming(7,4) method
    coded_sig = encode_signal(bin_signal)
    # add noise to the encoded signal
    n_coded_sig = add_noise(coded_sig)
    # decode the noised signal
    n_bin_sig = decode_signal(n_coded_sig)
    # convert back into an array of int values
    n_signal = convert_int(n_bin_sig)
    # save the decoded signal into a new file
    write_wav('n_sound.wav', 11025, data)
    # display the decoded signal
    print_wav('n_sound.wav', "noised sound")
