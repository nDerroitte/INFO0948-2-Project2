from util import *
from CST import *


class Huffman:
    def __init__(self):
        self.length = 0
        self.huffman_dict = {}

    def binaryHuffmanCoding(self, dict):
        """
        From a probability distribution, compute the binary huffman coding
        """
        self.huffman_dict, tmp = self.binaryHuffmanCodingAux(dict)
        self.length += tmp
        return self.huffman_dict


    def binaryHuffmanCodingAux(self, dict):
        """
        From a probability distribution, compute the binary huffman coding
        Auxialary function used in order to set the huffman class wiht the good
        dict and good length
        """
        if(len(dict) == 2):
            k1  = lowestKeyDict(dict)
            v1 = dict.pop(k1)
            k2 = lowestKeyDict(dict)
            v2 = dict.pop(k2)
            return {k1 : '1', k2 : '0'}, v1+v2

        k1 = lowestKeyDict(dict)
        v1 = dict.pop(k1)
        k2 = lowestKeyDict(dict)
        v2 = dict.pop(k2)
        dict[k1 + k2] = v1 + v2

        huffman_dict, count = self.binaryHuffmanCodingAux(dict)
        self.length += count

        current_coding = huffman_dict.pop(k1 + k2)
        huffman_dict[k1] = current_coding + '1'
        huffman_dict[k2] = current_coding + '0'
        return huffman_dict, v1 + v2

    def encode(self):
        """
        Enocde the text.csv file using the huffman encoding
        """
        str_out = ""
        f = open(CST.TEXT_FILE, "r")
        char = f.read(1)
        # While not at the EOF
        while char:
            # Put in lowercase
            if char.isupper():
                char = char.lower()
            str_out+= self.huffman_dict[char]
            char = f.read(1)
        return str_out
