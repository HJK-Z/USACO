if __name__ == '__main__':
    fin = open('photo.in', 'r')
    fout = open('photo.out', 'w')
    N = int(fin.readline())
    bstr = fin.readline().strip().split()

    # N = int(input())
    # bstr = input().split()

    b = [int(bstr[i]) for i in range(len(bstr))]

    for a1 in range(1, N+1):
        used = [False]*(N+1)
        prev = a1

        works = True
        A = []
        for i in range(N-1):
            if prev <= 0 or prev > N or used[prev]:
                works = False
                break
            A.append(prev)
            used[prev] = True
            prev = b[i] - prev

        if prev <= 0 or prev > N or used[prev]:
            works = False

        if works:
            # for i in range(N-1):
            #     print(A[i], end=" ")
            # print(prev)
            for i in range(N-1):
                fout.write(str(A[i])+" ")
            fout.write(str(prev))
            break

    fout.close()
