def ff(x, y):
    cx = [0, 0, 1, -1]
    cy = [1, -1, 0, 0]

    spots[count].append((x, y))
    grid[x][y] = 0
    for i in range(4):
        nx = x+cx[i]
        ny = y+cy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] != 0:
                ff(nx, ny)


N, M = map(int, input().split())

grid = [[0]*M for i in range(N)]
for i in range(N):
    tmparr = input()
    for j in range(len(tmparr)):
        if tmparr[j] == '.':
            grid[i][j] = 0
        else:
            grid[i][j] = 1

spots = [[], []]
count = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] != 0:
            ff(i, j)
            count += 1

mindist = 501230
for spot1 in spots[0]:
    for spot2 in spots[1]:
        dist = abs(spot1[0]-spot2[0]) + abs(spot1[1]-spot2[1]) - 1
        mindist = min(mindist, dist)

print(mindist)