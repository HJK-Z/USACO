if __name__ == '__main__':
    fin = open('triangles.in', 'r')
    fout = open('triangles.out', 'w')
    N = int(fin.readline().strip())
    posts = []
    for i in range(N):
        x, y = map(int, fin.readline().strip().split())
        posts.append((x, y))

    # N = int(input())
    # posts = []
    # for i in range(N):
    #     x, y = map(int, input().split())
    #     posts.append((x, y))

    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i!=j and j!=k and k!=i:
                    x1, y1 = posts[i]
                    x2, y2 = posts[j]
                    x3, y3 = posts[k]

                    if x1==x2 or x1==x3 or x2==x3:
                        if y1==y2 or y1==y3 or y2==y3:
                            ans = max(ans, abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))

    # print(ans)

    fout.write(str(ans))
    fout.close()
