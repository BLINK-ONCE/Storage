import time

N = int(input('N = '))
startTime = time.time()
sum = 0

for i in range(1, N + 1):
    sum += i
print('sum is:', sum)
print('It takes', time.time() - startTime, 'seconds')