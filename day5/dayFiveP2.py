f = open('C:\\adventureOfCode\\day5\\list.txt', 'r', encoding="utf8")
arr = []
auxArr = []
auxArr1 = []
auxAppend = []

for line in f:
  lineS = line.split()
  if lineS == []:
    pass
  elif lineS[0].isnumeric():
    for n in range(0,int(lineS[-1])):
      arr.append([])
      breaker = True
    for l in reversed(range(len(auxArr))):
      i = 0
      for letter in range(1, len(auxArr[l]), 4):
        if auxArr[l][letter].isspace():
          i += 1
        elif auxArr[l][letter].isalpha():
          arr[i].append(auxArr[l][letter])
          i += 1
  elif lineS[0] == "move":
    auxArr1.append(lineS[1])
    auxArr1.append(lineS[3])
    auxArr1.append(lineS[5])
    for i in range(int(auxArr1[0])):
      auxAppend.append(arr[int(auxArr1[1])-1][-1])
      arr[int(auxArr1[1])-1].pop()
    for i in range(int(auxArr1[0])): 
      arr[int(auxArr1[2])-1].append(auxAppend[-1])
      auxAppend.pop()
    auxArr1.clear()
  auxArr.append(line.replace("\n",""))


for final in arr:
  print(final[-1], end= "")
