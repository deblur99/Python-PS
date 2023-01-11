till = int(input())
if till > 100:
  till = 100
for i in range(1, till+1):
  if i % 3 == 0:
    continue
  print(i, end=' ')