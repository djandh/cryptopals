
from binascii import hexlify, unhexlify
from Crypto.Util.strxor import strxor

#plaintext = b'''Burning 'em, if you ain't quick and nimble
#I go crazy when I hear a cymbal'''
#key = b"ICE"
result = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a2622632427\
2765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"


plaintext = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
key = "ICE"


def repeatingKeyXor(plain, key):
    plain = str.encode(plain)
    key = str.encode(key)
    return bytes([plain[i] ^ key[i % len(key)] for i in range(len(plain))])

def repeatingKeyXor_v2(plain, key):
    result = []
    for i in range(len(plain)):
        plainEnc = str.encode(plain[i])
        keyEnc = str.encode(key[i%len(key)])
        result.append(strxor(plainEnc, keyEnc))
    return b''.join(result)


if __name__=='__main__':

    answer = repeatingKeyXor(plaintext, key)
    encodedAns = hexlify(answer).decode('ascii')
    print(encodedAns)
    #print(result)

    myAns = repeatingKeyXor_v2(plaintext, key)
    print(hexlify(myAns).decode() == result)




