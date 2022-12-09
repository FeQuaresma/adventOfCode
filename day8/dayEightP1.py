f = open("C:\\adventureOfCode\\day8\\list1.txt", "r", encoding="utf8")
grid = []
i = 0 
sumTotal = 0
blockSide = [[],[],[],[]]

for line in f:
  grid.append([])
  for l in line:
    if l != "\n":
      grid[i].append(l)
  i += 1

for row in range(len(grid)):
  for col in range(len(grid)):
    for index in range(1, len(grid)):
      if blockSide == ["blocked","blocked","blocked","blocked"]:
        blockSide = [[],[],[],[]]
        break
      if (col-index < 0 and blockSide[3] == []) or (row-index < 0 and blockSide[2] == []) or (col+index > len(grid)-1 and blockSide[1] == []) or (row+index > len(grid)-1 and blockSide[0] == []):
        sumTotal += 1
        print(grid[row][col], "escapou")
        blockSide = [[],[],[],[]]
        break

      if row+index <= len(grid)-1:
        if grid[row][col] <= grid[row+index][col]:
          blockSide[0] = "blocked"
      if col+index <= len(grid)-1:
        if grid[row][col] <= grid[row][col+index]:
          blockSide[1] = "blocked"
      if row-index >= 0:
        if grid[row][col] <= grid[row-index][col]:
          blockSide[2] = "blocked"
      if col-index >= 0:
        if grid[row][col] <= grid[row][col-index]:
          blockSide[3] = "blocked"        
      
print(sumTotal)