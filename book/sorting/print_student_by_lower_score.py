import sys
input = sys.stdin.readline

N = int(input())
arr = {}
for _ in range(N):
  A, B = input().split()
  arr[A] = int(B)

result = list(arr.keys())
result = sorted(result, key=lambda k: arr[k])
print(result)