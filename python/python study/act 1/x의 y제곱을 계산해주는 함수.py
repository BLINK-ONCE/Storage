def power(x, y):
    result = x
    for i in range(y - 1):
        result *= x
    return result

a = int(input('a = '))
b = int(input('b = '))

print(power(a, b))