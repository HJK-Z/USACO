def rumsev(group):
    group.sort()
    comdiff = group[0]-chord[0]

    for i in range(len(group)):
        if group[i]-chord[i] != comdiff:
            return False

    return True

N = int(input())
notes = []
for i in range(N):
    notes.append(int(input()))

C = int(input())
chord = []
for i in range(C):
    chord.append(int(input()))
chord.sort()

ans = []
for i in range(N-C+1):
    group = notes[i:i+C]
    if rumsev(group):
        ans.append(i+1)

print(len(ans))
for i in range(len(ans)):
    print(ans[i])