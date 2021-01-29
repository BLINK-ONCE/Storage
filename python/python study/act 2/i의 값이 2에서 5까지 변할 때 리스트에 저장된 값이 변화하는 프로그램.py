def printList(i, list):
    print('i =', i)
    print('<list>')
    print(list)
    print('')

def changeListValue(i, N):
    listTemp = list(range(N + 1))
    for j in range(i, N + 1, i):
        listTemp[j] = 0
    printList(i, listTemp)

N = int(input('N = '))
print('<Init list>')
print(list(range(N + 1)))
print('')
for i in range(2, 5 + 1):
    changeListValue(i, N)