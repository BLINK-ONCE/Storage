while (1):
    print('input integer a, b, c, d')
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    d = int(input('d = '))

    print('before sorting:', a, b, c, d)

    if (c > d): c, d = d, c
    if (b > c): b, c = c, b
    if (a > b): a, b = b, a

    if (c > d): c, d = d, c
    if (b > c): b, c = c, b

    if (c > d): c, d = d, c


    print('after soring:', a, b, c, d)