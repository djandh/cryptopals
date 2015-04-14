
from singleByteXor import *
from binascii import unhexlify

def detectSingleCharXor(fileName):

    scores, msg = [], ""

    with open(fileName, 'r') as f:
        
        for line in f:

            if line[-1] == '\n':
                line = line[:-1]
            decoded = breakSingleByteXor(unhexlify(line))
            # decoded[0] is the message, decoded[2] is the score
            scores.append(decoded[2])
            if decoded[2] >= max(scores):
                msg = decoded[0]

    return msg


if __name__=='__main__':

    msg = detectSingleCharXor("4.txt")
    print(msg)



