def swap(start, end, cows):
    if start == 1:
        cows[start-1:end] = cows[end-1::-1]
        return
    cows[start-1:end] = cows[end-1:start-2:-1]

def process(cows):
    swap(A1,A2,cows)
    swap(B1,B2,cows)

if __name__ == '__main__':
    fin = open('swap.in', 'r')
    fout = open('swap.out', 'w')
    N, K = map(int, fin.readline().strip().split())
    A1, A2 = map(int, fin.readline().strip().split())
    B1, B2 = map(int, fin.readline().strip().split())

    # N, K = map(int, input().split())
    # A1, A2 = map(int, input().split())
    # B1, B2 = map(int, input().split())

    cows = [i for i in range(N)]

    sort = False
    t = 0
    while not sort and t < K:
        t += 1
        process(cows)
        sort = True
        for i in range(N):
            if cows[i] != i:
                sort = False
                break

    left = K % t

    ans = cows.copy()
    while left != 0:
        process(ans)
        left -= 1

    # for i in range(N):
    #     print(ans[i]+1)

    for i in range(N):
        fout.write(str(ans[i] + 1)+"\n")
    fout.close()
