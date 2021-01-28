N = int(input('N = '))
odd = int(input("choose odd or not(1: odd, 2: not): "))

if (odd == 1):# when it is odd
    for i in range(1, N + 1):
        if (i % 2): print(i, end=' ')
elif (odd == 2):
    for i in range(2, N + 1):
        if (i % 2 == 0): print(i, end=' ')
else:
    print('input error')