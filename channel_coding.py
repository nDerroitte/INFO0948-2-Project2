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

def convert_binary(array):
    bin_array = []
    for value in array:
        bin_array.append([int(x) for x in '{0:08b}'.format(value)])
    return np.array(bin_array)

def bin_array_to_int(bin_array):
    value = 0
    for bit in bin_array:
        value = (value << 1) | bit
    return value

def convert_int(bin_signal):
    array = np.zeros(len(bin_signal), dtype=int)
    for i in range(len(bin_signal)):
        array[i] = bin_array_to_int(bin_signal[i])
    return array

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

def corr_coded_sig(n_coded_sig):
    c_coded_sig = np.zeros((len(n_coded_sig), 14), dtype=int)
    for i in range(len(coded_sig)):
        c_coded_sig[i][:7] = correct(n_coded_sig[i][:7])
        c_coded_sig[i][7:] = correct(n_coded_sig[i][7:])
    return c_coded_sig

def parity_check(code):
    return np.mod(np.dot(H, code), 2)

def correct(code):
    c_code = code.copy()
    err_index = max(bin_array_to_int(parity_check(code)) - 1, 0)
    c_code[err_index] = invert_bit(c_code[err_index])
    return c_code

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
    # try to correct the n_signal
    c_coded_sig = corr_coded_sig(n_coded_sig)
    # decode the noised signal
    n_bin_sig = decode_signal(n_coded_sig)
    # convert back into an array of int values
    n_signal = convert_int(n_bin_sig)
    # save the decoded signal into a new file
    write_wav('n_sound.wav', 11025, data)
    # display the decoded signal
    print_wav('n_sound.wav', "noised sound")
