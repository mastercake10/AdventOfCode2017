#!/usr/bin/env python2

input = "31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33"

def calcKnotHash(lengths, rounds=1):
    ran = range(0, 256)
    pos = 0
    skip_size = 0
    for _ in range(rounds):
        for length in lengths:
            selected = []
            if (pos+length)%len(ran) < pos%len(ran):
                selected = ran[pos%len(ran):len(ran)] + ran[0:(pos+length)%len(ran)]
            else:
                selected = ran[pos%len(ran):(pos+length)%len(ran)]
            for idx, num in enumerate(selected[::-1]):
                ran[(pos + idx)%len(ran)] = num
            pos = (pos + length + skip_size) % len(ran)
            skip_size += 1
    return ran

def formatHexDigit(digit):
    if len(digit) == 3:
        return "0" + digit[2:3]
    return digit[2:4];

ran = calcKnotHash(map(int, input.split(",")))
print("Output part1: " + str(ran[0] * ran[1]))

bytes = map(ord, list(input)) + [17, 31, 73, 47, 23]
ran = calcKnotHash(bytes, 64)
densehash = []

for i in range(16):
    densehash.append(reduce(lambda x,y: x^y,ran[i*16:i*16+16]))
finalhash = "".join(map(lambda x: formatHexDigit(x), map(hex, densehash)))

print("Output part2: " + finalhash)
