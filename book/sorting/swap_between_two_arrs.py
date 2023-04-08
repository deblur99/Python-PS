import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()  # A는 오름차순으로
B.sort(reverse=True) # B는 내림차순으로 정렬

# A와 B의 크기를 비교하여, A의 요소가 B의 요소보다 작으면 B의 요소로 바꿔치기한다.
count = 0
for i in range(N):
  if A[i] >= B[i] or count >= 3:
    break  
  A[i], B[i] = B[i], A[i]
  count += 1

print(sum(A))