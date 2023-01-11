'''
h: 세로
w: 가로
n: 막대의 개수
l: 각 막대의 길이
d: 막대 놓는 방향 (0 - 가로, 1 - 세로)
x, y: 좌표
'''

h,w = list(map(lambda n: int(n), input().split()))
board = [[0 for i in range(w)] for i in range(h)]

n = int(input())
for i in range(n):
  l,d,x,y = list(map(lambda n: int(n), input().split()))
  if d == 0: # 가로 방향으로 놓기 -> row 고정
    for j in range(l):
      board[x-1][y-1+j] = 1
    
  elif d == 1: # 세로 방향으로 놓기 -> col 고정
    for j in range(l):
      board[x-1+j][y-1] = 1
      
for i in range(h):
  for j in range(w):
    print(board[i][j], end=' ')
  print()