f = open("C:\\adventureOfCode\\day7\\list1.txt", "r", encoding="utf8")
folders = {"/":{}}
crrtFolder = ["/"]
auxObj = {}

for line in f:
  auxFolder = folders[crrtFolder[0]]
  mastro = line.split()

  for folder in crrtFolder[1:]:
      auxFolder = auxFolder[folder]

  if mastro[0] == "dir":
    auxFolder[mastro[1]] = {}
  if mastro[0].isnumeric():
    auxFolder[mastro[1]] = mastro[0]

  if mastro[0] == "$" and mastro[1] != "ls":
    if mastro[2].isalpha():
      crrtFolder.append(mastro[2])
    elif mastro[2] == "/":
      crrtFolder = ["/"]
    else:
      crrtFolder.pop()

def sumFolder(atualFolder, folderName="/"):
  auxList = []
  for folder in atualFolder:
    if type(atualFolder[folder]) == dict:
      auxList.append(sumFolder(atualFolder[folder], str(atualFolder[folder])))
    else:
      auxList.append(int(atualFolder[folder]))
  auxObj[folderName] = sum(auxList)
  auxList.clear()
  return auxObj[folderName]
    
sumFolder(folders["/"])

finalList = list(auxObj.values())
auxlist2 = 0

print(sum(filter(lambda i : i <=100000, finalList)))
print(finalList[-1])