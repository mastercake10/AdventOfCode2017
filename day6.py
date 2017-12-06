#!/usr/bin/env python3

input = "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6"
banks = list(map(int, input.split()))
previousBanks, cys = [], 0

while banks not in previousBanks:

    cys+=1
    previousBanks.append(list(banks))
    maxBankValue = max(banks)
    i = banks.index(maxBankValue)
    banks[i] = 0

    for idx in range(maxBankValue, 0, -1):
        i = (i + 1) % len(banks)
        banks[i] += 1

print("Output part1: " + str(cys))
print("Output part1: " + str(len(previousBanks) - previousBanks.index(banks)))
