from nbSymbol import *
from probDistrib import *
from util import *
from huffman import *

if __name__ == "__main__":
    print("QUESTION 1:")
    alphabet = getAlphabet()
    print("Set of additional characters: {}".format(additionalCharacter(alphabet)))
    print("Number of symbols : {}".format(nbSymbols(alphabet)))
    print("QUESTION 2:")
    print("Marginal probability distribution of all symbols from the text sample:")
    prob_distrib, total_length = getProbDistrib(alphabet)
    printSortedDict(prob_distrib)
    print("QUESTION 3:")
    huff = Huffman()
    huffman_dict = huff.binaryHuffmanCoding(prob_distrib)
    printSortedDict(huffman_dict)
    print("QUESTION 4:")
    print("Encoding of the text file ...", end=' ')
    str_encode = huff.encode()
    print("  done! Uncomment in code to see the encoded text (quite large)")
    # UNCOMMENT HERE to see the encoded text
    # print(str_encode)
    print("Total length of the encoded text sample : {}".format(len(str_encode)))
    print("Total length of the not enconded text sample : {}".format(total_length))
    print("QUESTION 5:")
    print("Expected average length for this code : {}".format(huff.length))
    print("QUESTION 6:")
    print("Compression rate of the algoritm: {}".format(total_length/len(str_encode)))
