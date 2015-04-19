
from hexToBase64 import *
from fixedXor import *
import unittest

class TestSet1(unittest.TestCase):

    def test_hexToBase64(self):
        hexInput =\
        "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        b64Output =\
        "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEqual(hexToBase64(hexInput), b64Output, "hexToBase64 failed")

    def test_fixedXor(self):
       s1 = "1c0111001f010100061a024b53535009181c"
       s2 = "686974207468652062756c6c277320657965"
       ans = "746865206b696420646f6e277420706c6179"
       self.assertEqual(fixedXor(s1, s2), ans, "fixedXor failed")

    def test_singlyByteXor(self):
        # run file to check if result is meaningful plaintext
        pass


if __name__=='__main__':
    unittest.main()
