f = open('list.txt', 'r', encoding="utf8")
sumTotal = 0
arr1 = []
arr2 = []
auxN = ""

for line in f:
  for i in range(len(line.replace("\n", ""))):
    if line[i] == "-" or line[i] == ",":
      if len(arr1) > 1:
        arr2.append(int(auxN))
      else:
        arr1.append(int(auxN))
      auxN = ""
    else:
      auxN = f'{auxN}{line[i]}'
  arr2.append(int(auxN))
  auxN = ""
  if (arr1[0] in range(arr2[0], arr2[1]+1)) or (arr1[1] in range(arr2[0], arr2[1]+1)) or (arr2[0] in range(arr1[0], arr1[1]+1)) or (arr2[1] in range(arr1[0], arr1[1]+1)):
    sumTotal += 1
  arr1.clear()
  arr2.clear()

print(sumTotal)