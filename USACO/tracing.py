if __name__ == '__main__':
    fin = open('tracing.in', 'r')
    fout = open('tracing.out', 'w')
    N, T = map(int, fin.readline().strip().split())
    cowsstr = fin.readline().strip()
    cows = [int(cowsstr[i]) for i in range(len(cowsstr))]

    shakes = []
    for i in range(T):
        time, x, y = map(int, fin.readline().strip().split())
        shakes.append((time, x - 1, y - 1))

    # N, T = map(int, input().split())
    # cowsstr = input()
    # cows = [int(cowsstr[i]) for i in range(len(cowsstr))]
    #
    # shakes = []
    # for i in range(T):
    #     time, x, y = map(int, input().split())
    #     shakes.append((time, x-1, y-1))

    shakes.sort(key=lambda shake: shake[0])

    patients = [False]*N
    Kmin = 100000
    Kmax = 0
    for patient in range(N):
        if cows[patient] == 1:
            # patient 0
            for K in range(252):
                works = True
                handshakesleft = [-1]*N
                handshakesleft[patient] = K
                for ts in range(T):
                    time, x, y = shakes[ts]
                    if handshakesleft[x] > 0:
                        if handshakesleft[y] == -1:
                            handshakesleft[y] = K
                        else:
                            handshakesleft[y] = max(0, handshakesleft[y]-1)

                        handshakesleft[x] -= 1
                    elif handshakesleft[y] > 0:
                        if handshakesleft[x] == -1:
                            handshakesleft[x] = K
                        else:
                            handshakesleft[x] = max(0, handshakesleft[x]-1)

                        handshakesleft[y] -= 1

                for i in range(N):
                    if cows[i] == 1 and handshakesleft[i] == -1 or cows[i] == 0 and handshakesleft[i] >= 0:
                        works = False
                        break

                if works:
                    patients[patient] = True
                    Kmin = min(Kmin, K)
                    Kmax = max(Kmax, K)

    patientposs = 0
    for i in range(N):
        if patients[i]:
            patientposs += 1

    if Kmax == 251:
        Kmax = "Infinity"

    # print(patientposs, Kmin, Kmax)
    fout.write(str(patientposs) + " " + str(Kmin) + " " + str(Kmax))
    fout.close()
