def max3(x, y, z):
    max = x
    if (max < y): max = y
    if (max < z): max = z
    return max


a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

print('22maximum value is', max3(a, b, c))