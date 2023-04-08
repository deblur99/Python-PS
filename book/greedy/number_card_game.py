import sys
input = sys.stdin.readline

result = 0

deck = []

N, M = list(map(int, input().split()))
for _ in range(N):
  deck.append(list(map(int, input().split())))

# 1. 뽑고자 하는 카드가 포함되어 있는 행을 선택
# 2. 선택한 행에 포함된 카드들 중 가장 작은 값 카드 선택
# -> 가장 작은 값이 가장 큰 값인 행을 선택하자.
for i in range(len(deck)):
  deck[i].sort()

max_idx = 0
for i in range(len(deck)):
  if deck[max_idx][0] < deck[i][0]:
    max_idx = i
  
print(deck[max_idx][0])

