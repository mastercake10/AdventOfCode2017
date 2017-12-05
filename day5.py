#!/usr/bin/env python3

from itertools import count

raw_input = []
with open("inputs/day5.txt") as file:
    raw_input = file.readlines()
input_list = list(map(int, raw_input))

idx = 0
length = len(raw_input)
for cnt in count(1):
    data_at_idx = input_list[idx]
    input_list[idx] += 1
    idx += data_at_idx
    if idx >= length:
        print("Output part1: " + str(cnt))
        break

input_list = list(map(int, raw_input))
idx = 0
for cnt in count(1):
    data_at_idx = input_list[idx]
    input_list[idx] += -1 if data_at_idx > 3 else 1
    idx += data_at_idx - 1
    if idx >= length:
        print("Output part2: " + str(cnt))
        break
