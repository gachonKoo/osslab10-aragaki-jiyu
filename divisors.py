try:
  x = input()
except:
  print('Error')
x = int(x)
y = list()
for i in range(1,x):
  if (x % i == 0):
    y.append(i)
print(*y)  
