N = int(input())

for i in range(1, N+1):
  value = i%10
  printed = str(value)
  for j in range(i):
    print(printed, end='')
  print()