board = [[0 for i in range(19)] for i in range(19)]

# input 값에 따라 업데이트
n = int(input())
for i in range(n):
  x, y = list(map(lambda n: int(n), input().split()))
  board[x-1][y-1] = 1

for i in range(19):
  for j in range(19):
    print(board[i][j], end=' ')
  print()