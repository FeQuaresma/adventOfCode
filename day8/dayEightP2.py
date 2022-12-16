f = open("C:\\adventureOfCode\\day8\\list1.txt", "r", encoding="utf8")
grid = []
i = 0
blockSide = [[], [], [], []]
scenicScore = [0, 0, 0, 0]
multiTotal = 0

for line in f:
    grid.append([])
    for l in line:
        if l != "\n":
            grid[i].append(l)
    i += 1

for row in range(len(grid)):
    for col in range(len(grid)):
        for index in range(1, len(grid)):
            if blockSide == ["blocked", "blocked", "blocked", "blocked"]:
                auxMulti = scenicScore[0] * scenicScore[1] * \
                    scenicScore[2] * scenicScore[3]
                if auxMulti > multiTotal:
                    multiTotal = auxMulti
                blockSide = [[], [], [], []]
                scenicScore = [0, 0, 0, 0]
                break

            if blockSide[0] != "blocked":
                if row+index > len(grid)-1:
                    blockSide[0] = "blocked"
                elif grid[row][col] > grid[row+index][col]:
                    scenicScore[0] += 1
                elif grid[row][col] <= grid[row+index][col]:
                    scenicScore[0] += 1
                    blockSide[0] = "blocked"

            if blockSide[1] != "blocked":
                if col+index > len(grid)-1:
                    blockSide[1] = "blocked"
                elif grid[row][col] > grid[row][col+index]:
                    scenicScore[1] += 1
                elif grid[row][col] <= grid[row][col+index]:
                    scenicScore[1] += 1
                    blockSide[1] = "blocked"

            if blockSide[2] != "blocked":
                if row-index < 0:
                    blockSide[2] = "blocked"
                elif grid[row][col] > grid[row-index][col]:
                    scenicScore[2] += 1
                elif grid[row][col] <= grid[row-index][col]:
                    scenicScore[2] += 1
                    blockSide[2] = "blocked"

            if blockSide[3] != "blocked":
                if col-index < 0:
                    blockSide[3] = "blocked"
                elif grid[row][col] > grid[row][col-index]:
                    scenicScore[3] += 1
                elif grid[row][col] <= grid[row][col-index]:
                    scenicScore[3] += 1
                    blockSide[3] = "blocked"

print(multiTotal)
