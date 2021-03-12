# http://www.usaco.org/index.php?page=viewproblem2&cpid=493

def finPos(i, max):
    finp = pos[i]+spd[i]*T

    if finp>max:
        return max

    return finp

if __name__ == '__main__':
    fin = open('cowjog.in', 'r')
    fout = open('cowjog.out', 'w')

    # N, T = map(int, input().split())
    N, T = map(int, fin.readline().strip().split())

    pos = []
    spd = []
    for i in range(N):
        # p, s = map(int, input().split())
        p, s = map(int, fin.readline().strip().split())

        pos.append(p)
        spd.append(s)

    lastMax = finPos(N-1, 1571238109248128719283675982371925689)
    groups = 1
    for i in range(N-2, 0-1, -1):
        nxtpos = finPos(i, lastMax)
        if nxtpos < lastMax:
            lastMax = nxtpos
            groups += 1


    # print(str(groups))
    fout.write(str(groups))
    fout.close()
