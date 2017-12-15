#!/usr/bin/env python2

# absolutely inefficient method, watch your ram usage!

START1 = 634
START2 = 301
FACTOR1 = 16807
FACTOR2 = 48271
DIV = 2147483647

def main():
    solvepart1()
    solvepart2()

def getMatchingBinaries(list1, list2, length):
    cnt = 0;
    for i in range(length):
        val1 = list(bin(list1[i])[2:].zfill(32))[-16:]
        val2 = list(bin(list2[i])[2:].zfill(32))[-16:]
        if val1 == val2:
            cnt += 1
        if i % 100000 == 0:
            print("Progress (matching binaries): " + str((i / float(length)) * 100.0) + "%")
    return cnt

def solvepart2():
    global FACTOR1, FACTOR2, DEV
    last1 = START1
    last2 = START2
    found1 = []
    found2 = []
    while len(found1) < 5e6:
        last1 = (last1*FACTOR1)%DIV
        if last1 % 4 == 0:
            found1.append(last1)
            if len(found1) % 300000 == 0:
                print("Progress (finding multiplies): " + str(((len(found1) + len(found2)) / 10e6) * 100.0) + "%")
    while len(found2) < 5e6:
        last2 = (last2*FACTOR2)%DIV
        if last2 % 8 == 0:
            found2.append(last2)
        if len(found2) % 200000 == 0:
            print("Progress (finding multiplies): " + str(((len(found1) + len(found2)) / 10e6) * 100.0) + "%")
    cnt = getMatchingBinaries(found1, found2, int(5e6))
    print("Output part2: ", cnt)
def solvepart1():
    global FACTOR1, FACTOR2, DEV
    last1 = START1
    last2 = START2
    found1 = []
    found2 = []
    for i in range(int(40e6)):
        last1 = (last1*FACTOR1)%DIV
        found1.append(last1)
        last2 = (last2*FACTOR2)%DIV
        found2.append(last2)
        if len(found1) % 300000 == 0:
            print("Progress (generating generators): " + str((i / 40e6) * 100.0) + "%")
    cnt = getMatchingBinaries(found1, found2, int(4e7))
    print("Output part1: ", cnt)
if __name__ == '__main__':
   main()
