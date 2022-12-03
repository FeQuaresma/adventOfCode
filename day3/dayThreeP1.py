f = open('list.txt', 'r', encoding="utf8")
alphaPoints = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
sumTotal = 0
breaker = False

for line in f:
  lenLine = int(len(line)/2 - 0.5)
  a = line[0:lenLine]
  b = line[lenLine:-1]
  for itemA in a:
    for itemB in b:
      if itemA == itemB:
        sumTotal += alphaPoints.index(itemA)+1
        breaker = True
        break
    if breaker == True:
      breaker = False
      break

print(sumTotal)
