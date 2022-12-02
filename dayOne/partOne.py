f = open('list.txt', 'r', encoding="utf8")
mostCal = mostCalIndex = sumArr = iCal = 0
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

# print(arr)

for elf in arr:
    for cal in elf:
      sumArr += cal
    # if sumArr > mostCal:
    #   mostCal = sumArr
    #   mostCalIndex = iCal
    arr[iCal] = sumArr
    sumArr = 0
    iCal += 1

arr.sort()
# print(mostCal)
print(arr[-3] + arr[-2] + arr[-1])
