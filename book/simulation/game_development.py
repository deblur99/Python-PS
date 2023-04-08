import sys
input = sys.stdin.readline

result = 0

# 세로, 가로
N, M = list(map(int, input().split()))
# 행좌표, 열좌표, 방향
# 0~3까지 북 동 남 서
chr_row, chr_col, chr_dir = list(map(int, input().split()))
# 지도 정보
# 0 - 육지, 1 - 바다
MAP = []
for _ in range(N):
  MAP.append(list(map(int, input().split())))
  
print(MAP)

MAP[chr_row][chr_col] = 2 # init

# 1) 현재 위치, 현재 방향을 기준으로 이동할 방향 결정
def get_left_dir(direction):
  if direction - 1 < 0:
    return 3
  else:
    return direction - 1

def get_right_dir(direction):
  if direction + 1 > 3:
    return 0
  else:
    return direction + 1

dirs = [get_left_dir(chr_dir), chr_dir, get_right_dir(chr_dir), get_right_dir(get_right_dir(chr_dir))]

is_movable = True

while is_movable:
  for dir in dirs:
    print(chr_row, chr_col)
    
    is_moved = False
    if dir == 0:
      if chr_row - 1 >= 0 and MAP[chr_row - 1][chr_col] == 0:
        chr_row -= 1
        MAP[chr_row][chr_col] = 2
        result += 1
        is_moved = True
        
    if dir == 1:
      if chr_col + 1 < M and MAP[chr_row][chr_col + 1] == 0:
        chr_col += 1
        MAP[chr_row][chr_col] = 2
        result += 1
        is_moved = True
        
    if dir == 2:
      if chr_row + 1 < M and MAP[chr_row + 1][chr_col] == 0:
        chr_row += 1
        MAP[chr_row][chr_col] = 2
        result += 1
        is_moved = True
        
    if dir == 3:
      if chr_col - 1 >= 0 and MAP[chr_row][chr_col - 1] == 0:
        chr_col -= 1
        MAP[chr_row][chr_col] = 2
        result += 1
        is_moved = True
      
    # 이동할 수 있는 곳이 없을 때, 현재 이동 방향의 반대 방향으로 1칸 이동한다.
    # 반대 방향으로 이동할 수 없다면, 현위치에서 멈춘다.
    if not is_moved:
      if dir == 0:
        if chr_row + 1 < N and MAP[chr_row + 1][chr_col] != 1:
          chr_row += 1
          MAP[chr_row][chr_col] = 2
          result += 1
          is_moved = True
          break
        
      if dir == 1:
        if chr_col - 1 >= 0 and MAP[chr_row][chr_col - 1] != 1:
          chr_col -= 1
          MAP[chr_row][chr_col] = 2
          result += 1
          is_moved = True
          break
        
      if dir == 2:
        if chr_row - 1 >= 0 and MAP[chr_row - 1][chr_col] != 1:
          chr_row -= 1
          MAP[chr_row][chr_col] = 2
          result += 1
          is_moved = True
          break
      
      if dir == 3:
        if chr_col + 1 < M and MAP[chr_row][chr_col + 1] != 1:
          chr_col += 1
          MAP[chr_row][chr_col] = 2
          result += 1
          is_moved = True
          break

      if not is_moved:
        is_movable = False
        break

print(result)