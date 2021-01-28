N = 0
listA = []
while (1):
    N = int(input('enter natural number(exit is 999): '))
    if (N == 999): break
    if (listA.count(N) < 1):listA.append(N)

print(listA)