f = open('list.txt', 'r', encoding="utf8")
varHelper = sumHelper = sumTotal = 0

# LOSE    0
# DRAW    3
# WIN     6
# PEDRA   A  X
# PAPEL   B  Y
# TESOURA C  Z

dictArr = [
  "AX","AY","AZ","BX","BY","BZ","CX","CY","CZ"
]

for line in f:
  varHelper = line.replace("\n", "")
  if varHelper[2] == "X":
    sumHelper = 1
  elif varHelper[2] == "Y":
    sumHelper = 2
  elif varHelper[2] == "Z":
    sumHelper = 3
  if varHelper[0] == "A" and varHelper[2] == "X" or varHelper[0] == "B" and varHelper[2] == "Y" or varHelper[0] == "C" and varHelper[2] == "Z":
    sumTotal += sumHelper + 3
  elif varHelper[0] == "A" and varHelper[2] == "Z" or varHelper[0] == "B" and varHelper[2] == "X" or varHelper[0] == "C" and varHelper[2] == "Y":
    sumTotal += sumHelper
  elif varHelper[0] == "A" and varHelper[2] == "Y" or varHelper[0] == "B" and varHelper[2] == "Z" or varHelper[0] == "C" and varHelper[2] == "X":
    sumTotal += sumHelper + 6

print(sumTotal)
