#!/usr/bin/env python3

with open('inputs/day11.txt') as file:
    line = file.readline()

input = line.replace("\n", "").split(",")

dirs = {"n": {"x": 0, "y": -2},
        "e": {"x": 2, "y": 0},
        "s": {"x": 0, "y": 2},
        "w": {"x": -2, "y": 2},
        "ne": {"x": 1, "y": -1},
        "nw": {"x": -1, "y": -1},
        "se": {"x": 1, "y": 1},
        "sw": {"x": -1, "y": 1}}

x, y = 0, 0
maxDist = 0
for dir in input:
    x += dirs[dir]["x"]
    y += dirs[dir]["y"]
    dist = abs(x) + abs(y);
    if dist > maxDist:
        maxDist = dist
dist = abs(x) + abs(y);
print("Output part1: " + str(dist / 2))
print("Output part2: " + str(maxDist / 2))
