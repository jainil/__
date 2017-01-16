def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def main():
    quest = "32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904"

    possible_outputs = {}

    letters = range(ord('A'), ord('z'))
    for letter1 in letters:
        for letter2 in letters:
            possible_outputs[chr(letter1^letter2).encode('hex')] = (letter1, letter2)
        
    print possible_outputs

    with open('ciphers.txt') as f:
        c1 = f.readline()
        c2 = f.readline()
        xoro = strxor(quest, c1).encode('hex')
        xoro2 = strxor(quest, c2).encode('hex')
        

        ans1 = [possible_outputs.get(xoro[i:i+2], (0,0)) for i in range(0, len(xoro), 2)]
        # ans2 = [possible_outputs.get(xoro2[i:i+2], (0,0)) for i in range(0, len(xoro2), 2)]

        resp = ""
        for i in xrange(0, len(ans1)):
            a1 = ans1[i]
            # a2 = ans2[i]
            nc = ord(' ')
            if a1[0] == a1[1]:
                nc = ord('-')
            elif a1[0] == 0:
                nc = ord(' ')
            else:
                nc = a1[0]


            # print nc
            resp += chr(nc)

        print resp

if __name__ == "__main__":
    main()