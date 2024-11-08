import sys
x = sys.stdin.readline()
x = int(x)
y = list()
for i in range(1,t):
  if (t % i == 0):
    y.append(i)
print(*y)  
