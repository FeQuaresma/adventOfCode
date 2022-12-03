f = open('list.txt', 'r', encoding="utf8")
alphaPoints = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
arrHelper = []
sumTotal = 0

for line in f:
  arrHelper.append(line.replace("\n", ""))

for i in range(0, len(arrHelper), 3):
  for iAlpha in alphaPoints:
    if iAlpha in arrHelper[i] and iAlpha in arrHelper[i+1] and iAlpha in arrHelper[i+2]:
      sumTotal += alphaPoints.index(iAlpha)+1

print(sumTotal)
