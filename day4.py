#!/usr/bin/env python3

with open("inputs/day4.txt") as file:
    sum1, sum2 = 0, 0
    for line in file.readlines():
        x = set(line.split())
        if len(x) == len(line.split()):
            sum1 += 1
        z = set()
        for word in line.split():
            z.add("".join(sorted(word)))
        if len(z) == len(line.split()):
            sum2 += 1
print("Output part1: " + str(sum1))
print("Output part2: " + str(sum2))
