while (1):
    N = int(input('enter natural number: '))
    if (N < 1):
        print (N, "is not natural number")
        while (N < 1):
            N = int(input('enter natural number: '))
            if (N < 1): print(N, "is not natural number")

    print('every divisor of', N, ':', end=' ')
    for i in range(1, N + 1):
        if (N % i == 0): print(i, end=' ')

    print("")