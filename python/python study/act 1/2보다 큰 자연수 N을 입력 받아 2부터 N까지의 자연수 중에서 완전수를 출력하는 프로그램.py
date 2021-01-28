#완전수, perfect number

def isPerfect(a):
    sum = 0

    for i in range (1, int((a/2) + 1)):
        if (a % i == 0): sum += i

    if (sum == a): return 1
    else: return 0
import time
start = time.time()
N = int(input('N = '))
for i in range(2, N + 1):
    if(isPerfect(i) == 1): print(i, end=' ')
print('')
print("time:", time.time() - start)