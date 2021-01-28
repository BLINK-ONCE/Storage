#완전수, perfect number

a = int(input('a = '))
sum = 0

for i in range (1, int((a/2) + 1)):
    if (a % i == 0): sum += i

if (sum == a): print("a is perfect number")
else: print("a is not perfect number")