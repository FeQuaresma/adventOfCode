f = open('list.txt', 'r', encoding="utf8")
varHelper = sumHelper = sumTotal = 0

# LOSE    0 X
# DRAW    3 Y
# WIN     6 Z
# PEDRA   A  1
# PAPEL   B  2
# TESOURA C  3

for line in f:
  varHelper = line.replace("\n", "")
  if varHelper[2] == "X": # LOSE
    if varHelper[0] == "A":
      sumHelper = 3
    elif varHelper[0] == "B":
      sumHelper = 1
    elif varHelper[0] == "C":
      sumHelper = 2
    sumTotal += sumHelper
  elif varHelper[2] == "Y": # DRAW
    if varHelper[0] == "A":
      sumHelper = 1
    elif varHelper[0] == "B":
      sumHelper = 2
    elif varHelper[0] == "C":
      sumHelper = 3
    sumTotal += sumHelper + 3
  elif varHelper[2] == "Z": # WIN
    if varHelper[0] == "A":
      sumHelper = 2
    elif varHelper[0] == "B":
      sumHelper = 3
    elif varHelper[0] == "C":
      sumHelper = 1
    sumTotal += sumHelper + 6

print(sumTotal)
