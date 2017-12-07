#!/usr/bin/env python3

import re, collections

bottomprogram = ""
detailprograms, programsweight = {}, {}
resultWeights = []

def getWeight(program):
    weights = [getWeight(sub) for sub in detailprograms[program]]
    if len(set(weights)) > 1:
        rightVal = sorted(weights)[0]
        wrongVal = sorted(weights)[-1]
        delta = rightVal - wrongVal
        weightParent = programsweight[detailprograms[program][weights.index(wrongVal)]]
        resultWeights.append(delta + weightParent)
        return programsweight[program] + sum(weights)
    return programsweight[program] + sum(weights)


with open("inputs/day7.txt") as file:
    programs = []
    subprograms = []
    for line in file.readlines():
        line = line.replace(",", "").replace("\n","")
        name, sub, weight = line.split(" ")[0], line.split(" ")[3:], int(line.split("(")[1].split(")")[0])

        programsweight[name] = int(weight)
        detailprograms[name] = sub
        subprograms.extend(sub)
        programs.append(name)
    bottomprogram = list(set(programs) - set(subprograms))[0]
    print("Output part1: " + bottomprogram)

getWeight(bottomprogram)
print("Output part2: " + str(resultWeights[0]))
