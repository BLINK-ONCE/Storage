while (1):
    print('input integer a, b, c')
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))

    print('before sorting:', a, b, c)

    if (c < b): b, c = c, b
    if (b < a): a, b = b, a
    if (c < b): b, c = c, b

    print('after sorting:', a, b, c)