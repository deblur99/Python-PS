'''
base case
1) 맨 아래의 가장 오른쪽에 도착
2) 더 이상 움직일 수 없을 때
3) 먹이를 찾은 경우

general case
1) 오른쪽으로 갈 수 있을 때 (0) 오른쪽으로 감
2) 오른쪽에 벽 (1)이 있을 때는 아래쪽으로 감
'''
# 상수
BOARD_SIZE = 10

MOVABLE = 0
WALL = 1
FEED = 2
PASSED = 9

# 선언
global board
board = list()
for i in range(BOARD_SIZE):
  board.append(list(map(lambda n: int(n), input().split())))

def find_feed_path(y, x):        
  # Base case
  if y == BOARD_SIZE and x == BOARD_SIZE:
    return
  
  if board[y-1+1][x-1] == WALL and board[y-1][x-1+1] == WALL:
    board[y-1][x-1] = 9
    return
  
  if board[y-1][x-1] == FEED:
    board[y-1][x-1] = 9
    return
  
  # General case
  board[y-1][x-1] = 9

  # 오른쪽이 벽이 아니면 오른쪽으로 이동  
  if board[y-1][x-1+1] != WALL:
    return find_feed_path(y, x+1)
  
  # 오른쪽이 벽이므로 아래쪽으로 이동
  else:
    return find_feed_path(y+1, x)


find_feed_path(2, 2)

for i in range(BOARD_SIZE):
  for j in range(BOARD_SIZE):
    print(board[i][j], end=' ')
  print()