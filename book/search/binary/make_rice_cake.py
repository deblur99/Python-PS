import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

# 10 15 17 19
# M = 6 -> 자르고 나서 합한 것
# 제일 작은 값으로 자르는 것부터 시작하기?
result = 0
while sum(arr) > M:
  arr = list(filter(lambda item: item >= 0, map(lambda n: n - 1, arr)))
  result += 1
  
print(result)