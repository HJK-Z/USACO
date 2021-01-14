if __name__ == '__main__':
    fin = open('race.in', 'r')
    fout = open('race.out', 'w')

    # K, N = map(int, input().split())
    K, N = map(int, fin.readline().strip().split())

    maxs = K+1
    for xval in range(N):
        # x = int(input())
        x = int(fin.readline())

        tmin = K
        left = 1
        right = maxs

        lasts = 0
        while left <= right:
            s = int((left + right)/2)
            if s == lasts:
                break
            lasts = s

            up = s*(s+1) // 2
            down = up - x*(x-1)//2
            if x >= s:
                down = 0
            d = up + down

            last = min(x, s)
            if d - last >= K:
                right = s
                continue
            ht = int((K-d)/s)
            h = ht*s

            t = ht + s + s-x+1
            if x >= s:
                t -= s-x+1
            if h+d < K:
                t += 1

            # print(s, left, right, t, ht, d, up, down)
            tmin = min(tmin, t)
            left = s

        # print(tmin)
        fout.write(str(tmin)+'\n')


    fout.close()
