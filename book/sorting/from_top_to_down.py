import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
  arr.append(int(input()))
  
arr.sort(reverse=True)

for item in arr:
  print(item, end=' ')