N = int(input())
piles = []

total = 0
for i in range(N):
    pi = int(input())
    total += pi
    piles.append(pi)

avg = total/N

ans = 0
for i in range(N):
    if piles[i] > avg:
        ans += piles[i]-avg

print(int(ans))

