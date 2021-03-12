def dfs(x, y):
    global squares
    global sol

    if x == y == 4:
        if squares == 24-K:
            sol += 1
        return

    cx = [0, 0, 1, -1]
    cy = [1, -1, 0, 0]

    grid[x][y] = 0
    squares += 1
    for i in range(4):
        nx = x+cx[i]
        ny = y+cy[i]

        if 0<=nx<5 and 0<=ny<5:
            if grid[nx][ny] == 1:
                dfs(nx, ny)

    grid[x][y] = 1
    squares -= 1


K = int(input())

grid = [[1]*5 for i in range(5)]
for i in range(K):
    x, y = map(int, input().split())
    grid[x-1][y-1] = 0

squares = 0
sol = 0
dfs(0, 0)

print(sol)
