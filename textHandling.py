from CST import *

def getAlphabet():
    """
    Read the text.csv file and return the corresponding alphabet

    The text.csv file was modifed to remove the last line containing the URL
    """
    alphabet = []
    # File reading
    f = open(CST.TEXT_FILE, "r")
    char = f.read(1)
    # While not at the EOF
    while char:
        # Put in lowercase
        if char.isupper():
            char = char.lower()
        # Add to alphabet
        if char not in alphabet:
            alphabet.append(char)
        char = f.read(1)
    # Sort the alphaber
    alphabet.sort()
    return alphabet

def getSymbolCount(alphabet):
    """
    From the alphabet, determine the count of each symbols + the total count
    """
    char_count = 0
    # prob_distrib = [0 for i in range(len(alphabet))]
    dict_symbols = { i : 0 for i in alphabet }

    f = open(CST.TEXT_FILE, "r")
    char = f.read(1)
    # While not at the EOF
    while char:
        # Put in lowercase
        if char.isupper():
            char = char.lower()
        # Put in lowercase
        char_count +=1
        dict_symbols[char] +=1
        char = f.read(1)
    return dict_symbols, char_count
