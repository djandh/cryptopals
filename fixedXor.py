
s = "1c0111001f010100061a024b53535009181c"
t = "686974207468652062756c6c277320657965"
result = "746865206b696420646f6e277420706c6179"

def fixedXor(s,t):
    hexlst = [hex(int(i,16)^int(j,16))[2:] for i,j in zip(s,t)]
    return "".join(map(str, hexlst))


if __name__=='__main__':

    #print(fixedXor(s,t))
    assert(fixedXor(s,t) == result)

