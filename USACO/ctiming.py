def minutes(d, h, m):
    return d*24*60 + h*60 + m

# fin = open('ctiming.in', 'r')
# fout = open('ctiming.out', 'w')
# d, h, m = map(int, fin.readline().split())

d, h, m = map(int, input().split())

begin = minutes(11, 11, 11)
end = minutes(d, h, m)

if end < begin:
    print(-1)
else:
    print(end - begin)

# fout.write()
# fout.close()