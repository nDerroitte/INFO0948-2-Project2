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
    """
    Convert a array of data into a binary array representing the image
    """
    bin_array = []
    for value in array:
        bin_array.append([int(x) for x in '{0:08b}'.format(value)])
    return np.array(bin_array)

def bin_array_to_int(bin_array):
    """
    Convert a binary array into a int number
    """
    value = 0
    for bit in bin_array:
        value = (value << 1) | bit
    return value

def convert_int(bin_signal):
    """
    Convert a binary array into a int array of data representing the image
    """
    array = np.zeros(len(bin_signal), dtype=int)
    for i in range(len(bin_signal)):
        array[i] = bin_array_to_int(bin_signal[i])
    return array

def encode_signal(bin_signal):
    """
    Encode a binary signal using the hamming algoritm
    """
    coded_sig = np.zeros((len(bin_signal), 14), dtype=int)
    for i in range(len(bin_signal)):
        coded_sig[i][:7] = hamming(bin_signal[i][:4])
        coded_sig[i][7:] = hamming(bin_signal[i][4:])
    return coded_sig

def invert_bit(bit):
    """
    Simple function allowing to flip a bit
    """
    if bit:
        bit = 0
    else:
        bit = 1
    return bit

def add_noise(coded_sig):
    """
    Add noise to the sound signal by flipping bits with a probability of 1%
    """
    n_coded_sig = coded_sig.copy()
    for i in range(len(n_coded_sig)):
        for j in range(len(n_coded_sig[i])):
            if np.random.choice(2, 1, p=[0.99, 0.01]):
                n_coded_sig[i][j] = invert_bit(n_coded_sig[i][j])
    return n_coded_sig

def corr_coded_sig(n_coded_sig):
    """
    Return the corrected coded signal
    """
    c_coded_sig = np.zeros((len(n_coded_sig), 14), dtype=int)
    for i in range(len(c_coded_sig)):
        c_coded_sig[i][:7] = correct(n_coded_sig[i][:7])
        c_coded_sig[i][7:] = correct(n_coded_sig[i][7:])
    return c_coded_sig

def parity_check(code):
    """
    Perform the parity check
    """
    return np.mod(np.dot(H, code), 2)

def correct(code):
    """
    Correct a code using the hamming error reerting
    """
    c_code = code.copy()
    syn_vector = parity_check(code)[::-1]
    err_index = bin_array_to_int(syn_vector) - 1
    if err_index == -1:
        return  c_code
    else:
        c_code[err_index] = invert_bit(c_code[err_index])
        return c_code

def decode_signal(coded_sig):
    """
    Decode a coded signal
    """
    bin_signal = np.zeros((len(coded_sig), 8), dtype=int)
    for i in range(len(coded_sig)):
        bin_signal[i][:4] = rev_hamming(coded_sig[i][:7])
        bin_signal[i][4:] = rev_hamming(coded_sig[i][7:])
    return bin_signal

def hamming(bin_value):
    """
    Perfoming the hamming coding
    """
    return np.mod(np.dot(G, bin_value), 2)

def rev_hamming(code):
    """
    Decoding a hamming code
    """
    return np.dot(R, code)

def channel_coding():
    # load the signal from the file
    signal = read('sound.wav')[1]
    print("QUESTION 8:")
    # plot the original sound
    print_wav('sound.wav', 'original sound')
    print("Original signal plotted")
    print("QUESTION 9:")
    print("Original signal:")
    print(signal)
    print("Binary signal:")
    # convert the signal into a binary signal
    bin_signal = convert_binary(signal)
    print(bin_signal)

    print("QUESTION 10:")
    print("Encoded signal:")
    # encode the binary signal using the hamming(7,4) method
    coded_sig = encode_signal(bin_signal)
    print(coded_sig)

    print("QUESTION 11:")
    print("Adding noise..")
    # add noise to the encoded signal
    n_coded_sig = add_noise(coded_sig)
    print("Noisy signal:")
    print(n_coded_sig)
    # decode the noisy signal
    n_bin_sig = decode_signal(n_coded_sig)
    # convert back into an array of int values
    n_signal = convert_int(n_bin_sig)
    # compute the similarity with the original signal
    print("Similarity with the original signal:")
    compare(signal, n_signal)
    # save the noisy signal into a wav file
    write_wav('n_sound.wav', 11025, n_signal)
    # plot the noisy signal
    print_wav('n_sound.wav', 'noisy sound')
    print("Noisy signal plotted")
    print("QUESTION 12:")
    print("Corrected signal:")
    # try to correct the n_signal
    c_coded_sig = corr_coded_sig(n_coded_sig)
    # decode the corrected signal
    c_bin_sig = decode_signal(c_coded_sig)
    # convert back into an array of int values
    c_signal = convert_int(c_bin_sig)
    # compute the similarity with the original signal
    print("Similarity with the original signal:")
    compare(signal, c_signal)
    # save the decoded signal into a new file
    write_wav('c_sound.wav', 11025, c_signal)
    # plot the decoded signal
    print_wav('c_sound.wav', "corrected sound")

def compare(array_1, array_2):
    """
    Compare 2 signals to check the pourcentage of similarity
    """
    count = 0
    size = len(array_1)
    for i in range(len(array_1)):
        if array_1[i] == array_2[i]:
            count += 1
    print("Similarity : " + str(count/size))
