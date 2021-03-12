N = int(input())
photos = [[] for i in range(5)]

for i in range(5):
    for j in range(N):
        photos[i].append(int(input())-1)

before = [[0]*N for i in range(N)]
for p in range(5):
    for i in range(N):
        for j in range(i+1, N):
            before[photos[p][i]][photos[p][j]] += 1

ordering = [0]*N
for i in range(N):
    count = 0
    for j in range(N):
        if before[i][j] >= 3:
            count += 1
    ordering[i] = N-count

count = 1
for i in range(N):
    for j in range(N):
        if ordering[j] == count:
            count += 1
            print(j+1)


