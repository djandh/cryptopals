
import base64
import binascii

s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
result = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


# in python 2, replace binascii with s.decode('hex')

def hexToBase64(s): 
    return base64.b64encode(binascii.unhexlify(s)).decode('ascii')


if __name__=='__main__':
    
    print(hexToBase64(s))
    assert(hexToBase64(s) == result)
