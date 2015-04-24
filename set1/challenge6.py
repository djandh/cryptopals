
from base64 import b64decode
import challenge3 
import challenge5
import itertools

def hamming_dist(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Undefined for strings of unequal length")
    # uncomment for string arguments
    #s1 = s1.encode()
    #s2 = s2.encode()
    return sum([bin(s1[i]^s2[i]).count('1') for i in range(len(s1))])


def guessKeysize(text):
    
    keyScores = []
    for keysize in range(2,41):

        blocks = [text[i:i+keysize] for i in range(0, 10*keysize, keysize)][0:4]
        pairs = list(itertools.combinations(blocks, 2))
        scores = [hamming_dist(p[0], p[1])/float(keysize) for p in pairs]
        keyScores.append((keysize,sum(scores)/6))
        
    return min(keyScores, key=lambda x:x[1])


# given keysize, find the key used to encrypt "text"
def breakRepeatingKeyXor(text, keysize):

    blocks = [text[i:i+keysize] for i in range(0, len(text), keysize)]
    transposedBlocks = list(itertools.zip_longest(*blocks, fillvalue=0))
    key = [challenge3.breakSingleByteXor(bytes(x))[1] for x in transposedBlocks]
    return bytes(key)


if __name__=="__main__":
  
    text = b64decode(open('6.txt', 'r').read())
    keysize= guessKeysize(text)[0]

    # diagnostic
    #print(keysize) # 29
    #print(len(text)) # 2876
 
    key = breakRepeatingKeyXor(text, keysize)
    msg = challenge5.repeatingKeyXor(text, key)


