def convert(cow):
    if cow=="G":
        return 0
    return 1


if __name__ == '__main__':
    fin = open('breedflip.in', 'r')
    fout = open('breedflip.out', 'w')
    N = int(fin.readline())
    A = fin.readline().strip()
    B = fin.readline().strip()

    # N = int(input())
    # A = input()
    # B = input()

    Acows = [convert(A[i]) for i in range(N)]
    Bcows = [convert(B[i]) for i in range(N)]

    lastchange = False
    count = 0
    for i in range(N):
        if Acows[i] != Bcows[i]:
            if not lastchange:
                count += 1
            lastchange = True
        else:
            lastchange = False

    # print(count)

    fout.write(str(count))
    fout.close()
