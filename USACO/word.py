if __name__ == '__main__':
    fin = open('word.in', 'r')
    fout = open('word.out', 'w')
    N, K = map(int, fin.readline().strip().split())
    words = fin.readline().strip().split()

    # N, K = map(int, input().split())
    # words = input().split()

    currlen = 0
    currstr = ""
    for i in range(N):
        if i == 0:
            currlen = len(words[i])
            currstr = words[i]
        elif currlen + len(words[i]) > K:
            # print(currstr)
            fout.write(currstr+"\n")
            currlen = len(words[i])
            currstr = words[i]
        else:
            currlen += len(words[i])
            currstr += " " + words[i]

    # print(currstr)

    fout.write(currstr)
    fout.close()
