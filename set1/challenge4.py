
import challenge3
from binascii import unhexlify


def decodeLines(fileName):
    with open(fileName, 'r') as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            yield unhexlify(line)


#def detectSingleCharXor(fileName):
#
#    scores, msg = [], ""
#
#    with open(fileName, 'r') as f:
#        
#        for line in f:
#
#            if line[-1] == '\n':
#                line = line[:-1]
#            decoded = breakSingleByteXor(unhexlify(line))
#            # decoded[0] is the message, decoded[2] is the score
#            scores.append(decoded[2])
#            if decoded[2] >= max(scores):
#                msg = decoded[0]
#
#    return msg

def detectSingleByteXor(lines):

    maxScore = -1
    for line in lines:
        decoded = challenge3.breakSingleByteXor(line)
        if decoded[2] >= maxScore:
            maxScore = decoded[2]
            msg = decoded[0]
    return msg


if __name__=='__main__':

    #msg = detectSingleCharXor("4.txt")
    #print(msg)

    lines = decodeLines('4.txt')
    msg = detectSingleByteXor(lines)
    print(msg)


