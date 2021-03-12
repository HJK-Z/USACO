def price(gift):
    return gift[0] + gift[1]


def coupon(gift):
    return gift[0]/2 + gift[1]


N, B = map(int, input().split())
gifts = []
for i in range(N):
    p, s = map(int, input().split())
    gifts.append((p, s))

gifts.sort(key=price)

mxgifts = 0
total = 0
while total + price(gifts[mxgifts]) <= B:
    total += price(gifts[mxgifts])
    mxgifts += 1


# case 1:
tmpmx = mxgifts
for i in range(mxgifts, N):
    if total + coupon(gifts[i]) <= B:
        tmpmx += 1
        break

# case 2:
for i in range(mxgifts):
    tmptotal = total - gifts[i][0]/2
    tmpmxgifts = mxgifts
    while tmptotal + price(gifts[tmpmxgifts]) <= B:
        tmptotal += price(gifts[tmpmxgifts])
        tmpmxgifts += 1

    tmpmx = max(tmpmx, tmpmxgifts)

print(tmpmx)
