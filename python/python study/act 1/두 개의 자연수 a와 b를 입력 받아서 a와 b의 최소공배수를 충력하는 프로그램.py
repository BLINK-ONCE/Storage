# 최소공배수, least common multiple

a = int(input('a = '))
b = int(input('b = '))

multipleA = a
multipleB = b

while (1):
    if (multipleA < multipleB): multipleA += a
    elif (multipleA > multipleB): multipleB += b
    elif (multipleA == multipleB):
        print('least common multiple is', multipleA)
        break