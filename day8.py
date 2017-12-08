#!/usr/bin/env python3

input = []
with open("inputs/day8.txt") as file:
    input = file.read().splitlines()

vars = {}
peak = 0
for row in input:
    vars[row.split(" ")[0]] = 0
for row in input:
    condition = row.split()[4:]
    condition[0] = str(vars[condition[0]])
    if eval(''.join(condition)):
        num = int(row.split()[2]) if "inc" in row.split()[1] else -int(row.split()[2])
        vars[row.split()[0]] += num
    if vars[row.split()[0]] > peak:
        peak = vars[row.split()[0]]
print("Output part1: " + str(max(vars.values())))
print("Output part2: " + str(peak))
