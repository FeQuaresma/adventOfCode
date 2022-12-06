f = list(open("list.txt", "r", encoding="utf8"))
for i in range(len(f[0])):
  if len(set(f[0][i:i+14])) == 14:
    print(set(f[0][i:i+14]))
    print(i+14)
    break
