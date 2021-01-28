# 유클리드 호제법, Euclidean-algorithm

a = int(input('enter natural number a: '))
b = int(input('enter natural number b: '))

if (a < b): a, b = b, a# always a is bigger than b

while (1):
    if (b == 0): break
    temp = a % b
    a = b
    b = temp

print(a)