#!/usr/bin/env python3

input = 347991
n = 1
nearest = None
while True:
    # getting nearest odd perfect square cornern n
    if nearest is None or (input - n*n < nearest and n*n < input):
        nearest = input - n*n
    else:
        # n-1 is our Manhattan distance to the center, calc delta from corner to input
        print("Output part1: " + str(-(n - 1 - nearest)))
        break
    n += 2
