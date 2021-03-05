# http://www.usaco.org/index.php?page=viewproblem2&cpid=492

def dist(i1, i2):
    x1, y1 = locs[i1]
    x2, y2 = locs[i2]

    return abs(x1-x2)+abs(y1-y2)

def good(i, k, d):
    if i==0:
        return True
    for j in range(k,K+1):
        if 0<=disttr[i][k]<=d:
            return False

    return True

def dfs(i, k, d):
    if not good(i, k, d):
        return

    disttr[i][k] = d
    for j in range(k,-1,-1):
        nxt = i+j+1
        if nxt>=N:
            break
        dfs(nxt, k-j, d+dist(i, nxt))


if __name__ == '__main__':
    fin = open('marathon.in', 'r')
    fout = open('marathon.out', 'w')

    # N, K = map(int, input().split())
    N, K = map(int, fin.readline().strip().split())

    locs = []
    for i in range(N):
        # x, y = map(int, input().split())
        x, y = map(int, fin.readline().strip().split())

        locs.append((x, y))

    disttr = [[-1]*(K+1) for i in range(N)]
    dfs(0, K, 0)

    mn = 12390121024
    for i in range(K+1):
        if disttr[N-1][i]>=0:
            mn = min(mn, disttr[N-1][i])

    # print(disttr)
    # print(str(mn))
    fout.write(str(mn))
    fout.close()
