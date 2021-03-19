# http://www.usaco.org/index.php?page=viewproblem2&cpid=511

import bisect

if __name__ == '__main__':
    fin = open('stampede.in', 'r')
    fout = open('stampede.out', 'w')

    # N = int(input())
    N = int(fin.readline().strip())

    events = []
    for i in range(N):
        # x, y, r = map(int, input().split())
        x, y, r = map(int, fin.readline().strip().split())

        events.append(((-1-x)*r, y))
        events.append((-x*r, -y))

    events.sort(key=lambda c: c[0])
    # print(cows)
    seen = []
    group = []
    i = 0
    while i<2*N:
        j = i
        while j<2*N and events[i][0] == events[j][0]:
            y = events[j][1]
            if y>0:
                if y not in group:
                    bisect.insort_left(group, y)
            else:
                if -y in group:
                    group.remove(-y)
            j += 1

        if len(group)>0:
            seen.append(group[0])
        i = j

    # print(str(len(set(seen))))

    fout.write(str(len(set(seen))))
    fout.close()