# http://www.usaco.org/index.php?page=viewproblem2&cpid=512

def dijkstra(A, B):
    dist = [(cost[A][i], passes[A][i]) for i in range(1001)]
    visited = [False]*1001

    dist[A] = (0, 0)

    for i in range(1001):
        mn = INF
        ind = 0
        for j in range(1001):
            if not visited[j] and dist[j][0] < mn:
                mn = dist[j][0]
                ind = j

        visited[ind] = True

        for j in range(1001):
            if dist[j] != INF and not visited[j]:
                crd = dist[j][0]
                nd = dist[ind][0] + cost[ind][j]
                np = dist[ind][1] + passes[ind][j]
                if crd > nd:
                    dist[j] = (nd, np)

                if crd == nd and dist[j][1] > np:
                    dist[j] = (crd, np)


    print(dist[1:6])

    return dist[B]



if __name__ == '__main__':
    fin = open('cowroute.in', 'r')
    fout = open('cowroute.out', 'w')

    # A, B, N = map(int, input().split())
    A, B, N = map(int, fin.readline().strip().split())

    INF = 12312243121223123123124120
    cost = [[INF]*1001 for i in range(1001)]
    passes = [[INF]*1001 for i in range(1001)]
    for i in range(N):
        # c, m = map(int, input().split())
        # cities = list(map(int, input().split()))
        c, m = map(int, fin.readline().strip().split())
        cities = list(map(int, fin.readline().strip().split()))

        for j in range(m-1):
            for k in range(j+1, m):
                oc = cost[cities[j]][cities[k]]
                if oc > c:
                    cost[cities[j]][cities[k]] = c
                    passes[cities[j]][cities[k]] = k-j

    # for i in range(1,6):
    #     print(passes[i][1:6])

    res, ct = dijkstra(A, B)

    # for i in range(1, 6):
    #     print(cost[i][1:6])

    if res == INF:
        print("-1 -1")
        fout.write("-1 -1")
    else:
        print(str(res) + " " + str(ct))
        fout.write(str(res) + " " + str(ct))

    fout.close()