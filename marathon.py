# http://www.usaco.org/index.php?page=viewproblem2&cpid=492

def dist(l1, l2):
    x1, y1 = locs[l1]
    x2, y2 = locs[l2]

    return abs(x1-x2)+abs(y1-y2)

if __name__ == '__main__':
    # fin = open('marathon.in', 'r')
    # fout = open('marathon.out', 'w')

    N, K = map(int, input().split())
    # N, K = map(int, fin.readline().strip().split())

    locs = []
    for i in range(N):
        x, y = map(int, input().split())
        # x, y = map(int, fin.readline().strip().split())

        locs.append((x, y))

    dp = [[120398129501]*(K+1) for i in range(N)]
    
    for n in range(N):
        for k in range(K):
            mn = 10293120512
            for l in range(k):
                prv = n-l-1
                if prv<0:
                    break
                dp[n][k-l] = min(dp[n][k-l], dp[prv][k-l] + dist(prv, n))

    mn = 21039125801240
    for i in range(K+1):
        mn = min(mn, dp[N-1][i])
    print(dp)
    print(str(mn))
    # fout.write(str(mn))
    # fout.close()
