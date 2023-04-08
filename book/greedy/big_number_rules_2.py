import sys
input = sys.stdin.readline

result = 0

# N -> 요소의 개수, M -> 더하는 횟수, K -> 연속으로 같은 값 더할 수 있는 횟수
N, M, K = list(map(int, input().split()))
numbers = list(map(int, input().split()))

# 값 더하기
# 배열 내 주어진 수들을 M번 더하여 가장 큰 값 구하기
# 연속된 수를 K번 초과하여 더할 수는 없음
# 단, 같은 값이어도 인덱스가 다르면 다른 값 취급
numbers.sort(reverse=True)

# K+1회만큼 값을 블록으로 묶고
block_count = int(M / (K + 1))
rest_count = M % (K + 1)

# 나머지 값만큼 더한다.
result += (numbers[0] * K + numbers[1]) * block_count
result += numbers[0] * rest_count
  
print(result)