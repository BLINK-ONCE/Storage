def isPrime(num):
    for i in range (2, num):
        if (num % i == 0): return 0
    return 1

N = int(input('enter natural number over not less than 2: '))
for i in range(2, N + 1):
    if (isPrime(i)): print(i, end=' ')