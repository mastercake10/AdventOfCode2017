#!/usr/bin/env python3

with open('inputs/day9.txt') as file:
    line = file.readline()

total_score, garbage_score, depth = 0, 0, 0
is_garbage, next_char = False, False
for char in line:
    if is_garbage:
        if next_char:
            next_char = False
        elif char == '!':
            next_char = True
        elif char == '>':
            is_garbage = False
        else:
            garbage_score += 1
    else:
        if char == '{':
            depth += 1
        elif char == '}':
            total_score += depth
            depth -= 1
        elif char == '<':
            is_garbage = True

print('Output part1: ' + str(total_score))
print('Output part2: ' + str(garbage_score))
