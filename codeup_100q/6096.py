SIZE = 19

board = list()
for i in range(SIZE):
  board.append(list(map(lambda n: int(n), input().split())))

flip_count = int(input())
for i in range(flip_count):
  row,col = list(map(lambda n: int(n), input().split()))
  for i in range(SIZE):
    # 가로줄 뒤집기
    board[row-1][i] = 1 - board[row-1][i]
    # 세로줄 뒤집기
    board[i][col-1] = 1 - board[i][col-1]

for i in range(SIZE):
  for j in range(SIZE):
    print(board[i][j], end=' ')
  print()
    