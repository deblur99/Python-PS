a,m,d,n = list(map(lambda n: int(n), input().split()))
result = a

for i in range(1, n):
  result = result * m + d

print(result)