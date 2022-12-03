f = open('list.txt', 'r', encoding="utf8")

mostCal = mostCalIndex = iCal = 0
arr = []
arrHelper = []
iArr = 0

for line in f:
  if line == "\n":
    iArr += 1
    arr.append(arrHelper)
    arrHelper = []
  else:
    arrHelper.append(int(line.replace("\n", "")))
arr.append(arrHelper)

for elf in arr:
    sumArr = 0
    for cal in elf:
      sumArr += cal
    arr[iCal] = sumArr
    iCal += 1

arr.sort()
print(sum(arr[-3:len(arr)]))
