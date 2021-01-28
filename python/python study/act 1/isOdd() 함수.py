def isOdd(num):
    if (num % 2): return 1
    else: return 0

N = int(input("natural number N = "))
for i in range(1, N + 1):
    if (isOdd(i)): print(i, end=' ')