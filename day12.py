#!/usr/bin/env python3

inp = []
with open("inputs/day12.txt") as file:
    inp = file.read().splitlines()

programs = {}
group_cnt = 0
current_group = []
rootet_programs = set()

# calcs grouped programs, stores total count to the global var group_cnt
def calc_grouped_programs(prg):
  global group_cnt, cache
  # creating the current group list
  st = [prg] + programs[prg]
  if st in current_group:
    return
  else:
    current_group.append(st)
  for prgs in programs[prg]:
    rootet_programs.add(prg)
    # calling the method itself to achieve deep search
    calc_grouped_programs(prgs)
  group_cnt += 1

# reading the file input to a list
for row in inp:
  sp = row.replace(" ", "").split("<->")
  programs[sp[0]]=sp[1].split(",")

calc_grouped_programs("0")
print("Output part1:", group_cnt)

groups = []
for prg in programs:
  # skip programs that groups already have been calculated
  if prg in rootet_programs:
    continue
  # sort the current group and add it to the groups, sort it in order to compare
  current_group_sorted = sorted(current_group)
  if current_group_sorted not in groups:
    groups.append(current_group_sorted)
  # reset current group for next cycle
  current_group = []
  calc_grouped_programs(prg)

print("Output part2:", len(groups))
