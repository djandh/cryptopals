
from base64 import b64decode
from binascii import unhexlify, hexlify
import math
from singleByteXor import breakSingleByteXor

def hamming_dist(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Undefined for strings of unequal length")
    # uncomment for string arguments
    #s1 = s1.encode()
    #s2 = s2.encode()
    return sum([bin(s1[i]^s2[i]).count('1') for i in range(len(s1))])


def guessKeysize(text):
    keyScores = []
    for keysize in range(2,40):
        first = text[:keysize]
        second = text[keysize:2*keysize]
        keyScores.append((keysize, float(hamming_dist(first, second))/keysize))

    return min(keyScores, key=lambda x:x[1])


# list<bytes>, int -> list<bytes>
def splitInput(text, keysize):

    # split into blocks
    blocks = []
    numBlocks = math.floor(len(text) / keysize)
    for i in range(numBlocks):
        blocks.append(text[i*keysize:(i+1)*keysize])

    if text[keysize*numBlocks:] != b"":
        blocks.append(text[keysize*numBlocks:])
    return blocks


# list<bytes>, int -> list<bytes>
def transpose(blocks, keysize):

    # transpose blocks
    transposed = []
    for i in range(keysize):
        tBlock = b"".join([bytes([b[i]]) for b in blocks if len(b) > i])
        transposed.append(tBlock)
    return transposed


if __name__=="__main__":

    with open("6.txt", 'r') as f:
        
        text = b64decode(bytes(f.read(), "utf8"))
        keysize= guessKeysize(text)[0]
        numBlocks = math.floor(len(text) / keysize)

        # diagnostic
        #print(keyGuess) # 5, 1.2
        #print(len(text)) # 2876

        blocks = splitInput(text, keysize)
        tBlocks = transpose(blocks, keysize)
        
#        for b in tBlocks:
#            print(b)
#            print(len(b))

        plain = []
        for b in tBlocks:
            decryption = breakSingleByteXor(b)
            plain.append(decryption[0])
            print(decryption[1:])
        bytemsg = b"".join(transpose(plain, numBlocks))
        print(bytemsg)



