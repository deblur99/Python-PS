r,g,b = list(map(lambda n: int(n), input().split(' ')))
for i in range(r):
  for j in range(g):
    for k in range(b):
      print(f'{i} {j} {k}')
print(r*g*b)
# 경우의 수는 r*g*b 