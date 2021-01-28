def sumAvg(x, y, z):
    global _sum
    global _avg
    _sum = x + y + z
    _avg = _sum/3

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

sumAvg(a, b, c)

print("sum =", _sum)
print("average =", _avg)