tmpset = []
def createsets(pos):
    if pos == N:
        sets.append(tmpset.copy())
        return

    createsets(pos+1)
    tmpset.append(weights[pos])
    createsets(pos+1)
    tmpset.pop(len(tmpset)-1)

def addition(arr):
    mxlen = 0
    for a in arr:
        mxlen = max(mxlen, len(str(a)))

    strarr = ["0"*(mxlen-len(str(a)))+str(a) for a in arr]

    for i in range(mxlen):
        total = 0
        for j in range(len(arr)):
            total += int(strarr[j][i])

        if total >= 10:
            return False

    return True

N = int(input())
weights = []
for i in range(N):
    weights.append(int(input()))

sets = []
createsets(0)

mxgroup = 0
for set in sets:
    if addition(set):
        mxgroup = max(mxgroup, len(set))

print(mxgroup)
