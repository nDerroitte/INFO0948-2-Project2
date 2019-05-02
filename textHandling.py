from CST import *

def getAlphabet(size=1):
    """
    Read the text.csv file and return the corresponding alphabet

    The text.csv file was modifed to remove the last line containing the URL
    """
    alphabet = []
    # File reading
    f = open(CST.TEXT_FILE, "r")
    char = f.read(1)

    symbol = ""
    # While not at the EOF
    while char:
        # Put in lowercase
        if char.isupper():
            char = char.lower()
        symbol += char
        # Add to alphabet
        if len(symbol) == size:
            if symbol not in alphabet:
                alphabet.append(symbol)
            symbol = ""

        char = f.read(1)
    # Sort the alphaber
    alphabet.sort()
    return alphabet

def getSymbolCount(alphabet, size=1):
    """
    From the alphabet, determine the count of each symbols + the total count
    """
    char_count = 0
    # prob_distrib = [0 for i in range(len(alphabet))]
    dict_symbols = { i : 0 for i in alphabet }

    f = open(CST.TEXT_FILE, "r")
    char = f.read(1)
    symbol = ""
    # While not at the EOF
    while char:
        # Put in lowercase
        if char.isupper():
            char = char.lower()
        symbol += char
        if len(symbol) == size:
            char_count +=1
            dict_symbols[symbol] +=1
            symbol = ""
        char = f.read(1)
    return dict_symbols, char_count

def SimpleEncode():
    """
    Perform a simple encoding of the text file
    """
    text = ""
    f = open(CST.TEXT_FILE, "r")
    char = f.read(1)
    # While not at the EOF
    while char:
        # Put in lowercase
        if char.isupper():
            char = char.lower()
        # Put in lowercase
        text += char
        char = f.read(1)
    return bin(int.from_bytes(text.encode(), 'big'))

def getAlphabet_2():
    """
    Get the alphabet corresponding to two characters at a time
    """
    alphabet = []
    # File reading
    f = open(CST.TEXT_FILE, "r")
    char = f.read(1)
    symbol = ""
    # While not at the EOF
    while char:
        # Put in lowercase
        if char.isupper():
            char = char.lower()
        symbol += char

        if len(symbol) == 2:
            # Add to alphabet
            if symbol not in alphabet:
                alphabet.append(symbol)
            symbol = ""
        char = f.read(1)
    # Sort the alphaber
    alphabet.sort()
    return alphabet
