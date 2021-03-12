if __name__ == '__main__':
    fin = open('socdist1.in', 'r')
    fout = open('socdist1.out', 'w')
    N = int(fin.readline())
    stallsstr = fin.readline().strip()

    # N = int(input())
    # stallsstr = input()
    stalls = [int(stallsstr[i]) for i in range(len(stallsstr))]

    mindist = N
    firstfilled = -1
    lastfilled = -1
    maxdist = 0
    maxdist1 = 0

    for i in range(len(stalls)):
        if stalls[i] == 1:
            if firstfilled == -1:
                firstfilled = i
            if lastfilled != -1:
                dist = i-lastfilled
                mindist = min(mindist, dist)
                if dist>maxdist:
                    maxdist1 = maxdist
                    maxdist = dist
                elif dist>maxdist1:
                    maxdist1 = dist

            lastfilled = i

    lastdist = len(stalls)-lastfilled
    firstdist = firstfilled

    # case 1
    tmaxdist = maxdist
    tmaxdist1 = maxdist1
    if firstdist*2>tmaxdist:
        tmaxdist1 = tmaxdist
        tmaxdist = firstdist*2
    elif firstdist*2>tmaxdist1:
        tmaxdist1 = firstdist*2
    if lastdist*2>tmaxdist:
        tmaxdist1 = tmaxdist
        tmaxdist = lastdist*2
    elif lastdist*2>tmaxdist1:
        tmaxdist1 = lastdist*2
    tmpdist = int(tmaxdist/2)
    tmpdist1 = int(tmaxdist1/2)
    tmpmindist = min(mindist, tmpdist, tmpdist1)

    # case 2
    tmpdist = int(maxdist/3)
    tmpmindist1 = min(mindist, tmpdist)

    # case 3
    tmpdist = int((firstdist-1) / 2)
    tmpmindist2 = min(mindist, tmpdist)

    # case 4
    tmpdist = int((lastdist-1) / 2)
    tmpmindist3 = min(mindist, tmpdist)

    res = max(tmpmindist, tmpmindist1, tmpmindist2, tmpmindist3)

    # case 5
    if firstfilled == lastfilled == -1:
        res = N-1

    # print(res)
    fout.write(str(res))
    fout.close()
