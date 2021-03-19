from collections import OrderedDict

print("Before deleting:\n")
od = OrderedDict()
od[1] = 1
od[2] = 2
od[3] = 3
od[4] = 4

for key, value in od.items():
    print(key, value)

print("\nAfter deleting:\n")
od.pop(3)
for key, value in od.items():
    print(key, value)

print("\nAfter re-inserting:\n")
od[3] = 3
for key, value in od.items():
    print(key, value) 