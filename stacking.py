N, K = map(int, input().split())

stacks = [0]*(N+1)
for i in range(K):
    a, b= map(int, input().split())

    stacks[a-1] += 1
    stacks[b] -= 1

acctotal = [0]*N
acctotal[0] = stacks[0]
for i in range(1, N):
    acctotal[i] = acctotal[i-1] + stacks[i]

acctotal.sort()
print(acctotal[int(N/2)])