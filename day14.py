#!/usr/bin/env python2

from day10 import calcTraditionallyKnotHash, condenseKnotHash

input = "uugsqrei"
#10000001
#01000110
#01110000
#10000011
#test = [[1,0,0,0,0,0,0,1],[0,1,0,0,0,1,1,0],[0,1,1,1,0,0,0,0],[1,0,0,0,0,0,0,1]]
test = []
def hexListToBinary(hexlist):
    return map(lambda x: bin(x)[2:].zfill(8), hexlist)

currentPatch = []
patches = []
known = []

def getNeighboors(x,y):
    if x >= 0 and y >= 0 and x < len(test) and y < len(test[x]) and test[x][y] == 1 and [x, y] not in currentPatch and [x, y] not in known:
        currentPatch.append([x, y])
        known.append([x, y])
        getNeighboors(x, y)
    x2 = x + 1
    y2 = y
    if x2 >= 0 and y2 >= 0 and x2 < len(test) and y2 < len(test[x2]) and test[x2][y2] == 1 and [x2, y2] not in currentPatch and [x2, y2] not in known:
        currentPatch.append([x2, y2])
        known.append([x2, y2])
        getNeighboors(x2, y2)
    x2 = x - 1
    y2 = y
    if x2 >= 0 and y2 >= 0 and x2 < len(test) and y2 < len(test[x2]) and test[x2][y2] == 1 and [x2, y2] not in currentPatch and [x2, y2] not in known:
        currentPatch.append([x2, y2])
        known.append([x2, y2])
        getNeighboors(x2, y2)
    x2 = x
    y2 = y + 1
    if x2 >= 0 and y2 >= 0 and x2 < len(test) and y2 < len(test[x2]) and test[x2][y2] == 1 and [x2, y2] not in currentPatch and [x2, y2] not in known:
        currentPatch.append([x2, y2])
        known.append([x2, y2])
        getNeighboors(x2, y2)
    x2 = x
    y2 = y - 1
    if x2 >= 0 and y2 >= 0 and x2 < len(test) and y2 < len(test[x2]) and test[x2][y2] == 1 and [x2, y2] not in currentPatch and [x2, y2] not in known:
        currentPatch.append([x2, y2])
        known.append([x2, y2])
        getNeighboors(x2, y2)

def main():
    solvepart1()
    solvepart2()
def solvepart2():
    for i in range(128):
        string = input + "-" + str(i)
        knothash = calcTraditionallyKnotHash(list(string))
        densehash = condenseKnotHash(knothash)
        test.append(map(int,list("".join(hexListToBinary(densehash)))))

    global currentPatch
    for x in range(-1, len(test)):
        for y in range(-1, len(test[x])):
            getNeighboors(x, y)
            #print(currentPatch)
            neigh = sorted(currentPatch)
            #print(len(patches))
            if len(neigh) == 0:
                continue
            if neigh not in patches:
                patches.append(neigh)
            currentPatch = []
    print("Output part2: ", len(patches))
def solvepart1():
    counter = 0

    for i in range(128):
        string = input + "-" + str(i)
        knothash = calcTraditionallyKnotHash(list(string))
        densehash = condenseKnotHash(knothash)
        for l in "".join(hexListToBinary(densehash)):
            for e in list(l):
                if e == "1":
                     counter += 1
    print("Output part1: ", counter)
if __name__ == '__main__':
   main()
