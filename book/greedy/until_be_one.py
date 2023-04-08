import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))

# N - 1
# N // K
# 위 2개를 조합하여 1을 만드는 가장 적은 처리 횟수 출력
result = 0

while N // K > 0:
  # 나누어 떨어질 때까지 1 빼기
  while N % K != 0:
    N -= 1
    result += 1
  
  N //= K
  result += 1
  
while N - K > 1:
  N -= K
  result += 1
  
print(result)