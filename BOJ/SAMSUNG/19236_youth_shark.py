'''
4×4크기의 공간이 있고, 크기가 1×1인 정사각형 칸으로 나누어져 있다
공간의 각 칸은 (x, y)와 같이 표현하며, x는 행의 번호, y는 열의 번호이다
한 칸에는 물고기가 한 마리 존재한다. 각 물고기는 번호와 방향을 가지고 있다.
번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수이며,
두 물고기가 같은 번호를 갖는 경우는 없다. 방향은 8가지 방향(상하좌우, 대각선) 중 하나이다.

상어는 좌표상의 물고기를 먹고, 해당 좌표로 이동한다. 그리고 작은 번호의 물고기부터 이동한다.

물고기는 한 칸을 이동할 수 있고,
이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸,
이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다.
각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
-> 물고기의 이동 방향에 다른 물고기가 있으면, 그 물고기와 위치를 바꾼다!

상어는 한 번에 여러 칸을 이동할 수 있다.
이동 경로에 있는 물고기는 먹지 않는다.
물고기가 없는 칸으로는 이동할 수 없다.
상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다.
상어가 이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복된다.
'''

result = 0

shark = -1
number = [i for i in range(1, 17)]
direction = [i for i in range(1, 9)]

arr = [[] for _ in range(4)]


# 0) 초기화
class Block:
    def __init__(self, number: int, direction: int, position_row: int, position_col: int):
        self.number = number
        self.direction = direction
        self.position_row = position_row
        self.position_col = position_col

    def to_string(self):
        return f'{self.number}, {self.direction}, {self.position_row}, {self.position_col}'

    def clear(self):
        self.number = -1
        self.direction = -1


# 1) 처음에 상어가 (0, 0) 위치로 이동하고, 그 자리의 방향을 가진다.
def move_shark(shark: Block):
    if shark.position_row < 1 and shark.position_col < 1 and shark.direction < 1:
        # 좌표가 1부터 시작함에 유의
        shark.position_row = 1
        shark.position_col = 1

        global result
        result += arr[0][0].number

        shark.direction = arr[0][0].direction
        shark.position_row = arr[0][0].position_row
        shark.position_col = arr[0][0].position_col

        arr[0][0] = shark


def swap_fish(fish1: Block, fish2: Block):
    fish1.number, fish2.number = fish2.number, fish1.number
    fish1.direction, fish2.direction = fish2.direction, fish1.direction
    fish1.position_row, fish2.position_row = fish2.position_row, fish1.position_row
    fish1.position_col, fish2.position_col = fish2.position_col, fish1.position_col

    arr[fish1.position_row][fish1.position_col] = fish2
    arr[fish2.position_row][fish2.position_col] = fish1

    return (fish1, fish2)


# 반시계방향으로 45도 회전
def spin_fish(fish: Block):
    if fish.direction < 1:
        return

    fish.direction += 1
    if fish.direction > 8:
        fish.direction -= 8


# 2) 번호가 작은 물고기부터 45도 반시계 회전하면서 이동한다.
# def fish_movement(arr: list) -> list:
#     arr[]

# 3) 이때, 물고기가 이동할 수 있는 로직을 짜야 한다.

# 4) 모든 물고기가 이동하면 상어가 이동한다.


# Main
def main():
    for i in range(4):
        row = list(map(int, input().split()))
        for j in range(0, len(row), 2):
            arr[i].append(Block(row[j], row[j + 1], i, j // 2))

    shark = Block(-1, -1, -1, -1)  # 아직 들어가기 전

    # debug
    for i in range(4):
        for j in range(4):
            print(arr[i][j].to_string(), end='\t\t')
        print()

    # 상어 움직이고
    move_shark(shark)

    # debug
    print()
    for i in range(4):
        for j in range(4):
            print(arr[i][j].to_string(), end='\t\t')
        print()

    # debug
    print(arr[0][0].number, arr[0][0].direction)
    print(result)

    # 물고기들이 낮은 순서부터 이동한다.

ㅈ

if __name__ == '__main__':
    main()