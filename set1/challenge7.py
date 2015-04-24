
from Crypto.Cipher import AES
from base64 import b64decode

key = b"YELLOW SUBMARINE"

if __name__=='__main__':

    with open('7.txt', 'r') as f:
        cipher = AES.new(key)
        plain = cipher.decrypt(b64decode(f.read()))
        print(plain)
