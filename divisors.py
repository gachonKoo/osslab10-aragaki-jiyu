import sys
x = int(sys.argv[1])
y = list()
for i in range(1,x):
  if (x % i == 0):
    y.append(i)
print(*y)  
