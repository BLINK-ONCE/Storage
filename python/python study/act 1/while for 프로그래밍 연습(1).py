N = int(input('N = '))


"""
# while statement

i = 1
sum = 0
while (i <= N):
    sum += i
    i += 1

print(sum)
"""

# for statement

sum = 0
for i in range(1, N + 1):
    sum += i

print(sum)