from textHandling import *
from CST import *

def nbSymbols(alphabet):
    """
    Return the number of Symbols from the alphabet, ie its size
    """
    return len(alphabet)

def additionalCharacter(alphabet):
    """
    Get the "additional characters" set of the alphabet
    """
    add_char = []
    i = 0
    # We can do that since the alphabet is sorted
    while alphabet[i] != "0":
        add_char.append(alphabet[i])
        i +=1
    return add_char
