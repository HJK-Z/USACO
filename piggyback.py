# http://www.usaco.org/index.php?page=viewproblem2&cpid=491
import queue

def bfs(src):
    dist = [-1]*N

    q = queue.Queue()
    q.put((src,0))
    while not q.empty():
        i, cnt = q.get()

        if dist[i] != -1:
            continue

        dist[i] = cnt
        for cn in connections[i]:
            q.put((cn,cnt+1))

    return dist

if __name__ == '__main__':
    fin = open('piggyback.in', 'r')
    fout = open('piggyback.out', 'w')

    # B, E, P, N, M = map(int, input().split())
    B, E, P, N, M = map(int, fin.readline().strip().split())

    connections = [[] for i in range(N)]

    for i in range(M):
        # f1, f2 = map(int, input().split())
        f1, f2 = map(int, fin.readline().strip().split())
        f1 -= 1
        f2 -= 1

        connections[f1].append(f2)
        connections[f2].append(f1)

    d1 = bfs(0)
    d2 = bfs(1)
    dN = bfs(N-1)

    mn = 40000011923028301238
    for i in range(N):
        mn = min(mn, d1[i]*B+d2[i]*E+dN[i]*P)

    print(d1)
    print(d2)
    print(dN)
    print(str(mn))

    fout.write(str(mn))

    fout.close()
