# http://www.usaco.org/index.php?page=viewproblem2&cpid=492

def dist(i1, i2):
    x1, y1 = locs[i1]
    x2, y2 = locs[i2]

    return abs(x1-x2)+abs(y1-y2)

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

    dp = [[1231923123]*N for i in range(K+1)]
    dp[0][0] = 0
    for k in range(K+1):
        for n in range(N):
            l = n+1
            while l<N and k+l-n-1<=K:
                nxk = k+(l-n-1)
                nxn = l
                dp[nxk][nxn] = min(dp[nxk][nxn], dp[k][n]+dist(n,l))
                l += 1

    # print(dp)
    # print(str(dp[K][N-1]))
    fout.write(str(dp[K][N-1]))
    fout.close()