from heapq import *

if __name__ == '__main__':
    # fin = open('berries.in', 'r')
    # fout = open('berries.out', 'w')

    N, K = map(int, input().split())
    # N, K = map(int, fin.readline().strip().split())

    # value, part, prevpartind
    trees = [(int(i), -1, None) for i in input().split()]

    pq = nlargest(K, trees)

    print(pq)

    splits = {}
    while False:
        n = 1
        largest = nlargest(1, pq)[0]
        nthsmall = heappop(pq)
        while largest / n > nthsmall[0]:
            n += 1
            if nthsmall[1] != -1:
                
            nthsmall = heappop(pq)

        if n == 1:
            break

    print()
    # fout.write(str(tmin)+'\n')
    #
    # fout.close()
