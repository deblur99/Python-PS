import sys

input = sys.stdin.readline

# input 값 받기
N, M, K = list(map(int, input().split()))
MAP = []
for i in range(N):
    MAP.append(list(map(int, input().split())))

# 좌표
position = [1, 1]

# 좌표 참조하기
# MAP[position[0]][position[1]]

# 주사위
# 방향 -> 키, 숫자 -> 값
dice = {
    'top': 1,
    'right': 3,
    'bottom': 6,
    'left': 4,
    'up': 2,
    'down': 5
}
dice_values = list(dice.values())

# 주사위 이동 방향
# 주사위는 1~6까지 있고,
dice_direction = {
    'up': 1,
    'right': 2,
    'down': 3,
    'left': 4
}

# 점수
# 같은 칸을 밟아야 점수 누적
# 점수 = 밟은 횟수 * 좌표 번호
point = 0


# 주사위 첫 이동

# 순서 정하기
# 1. 주사위 동서남북 회전 구현하기 (성공)
# 2. 처음 주사위 이동 구현하기
# 3. 주사위 아랫면과 현위치 값 비교하여 주사위 이동방향 회전시키기
# 4. 점수 구하기

# 1. 주사위 동서남북 회전 구현하기
def spin_dice(dice: dict = dice, direction: int = 1):
    # 1부터 4까지 동서남북 순
    temp = []

    if direction == 1 or direction == 2:
        if direction == 1:  # 동쪽 회전
            # left, top, right, bottom 자리에 올 값 순서대로 들어감
            temp.append(dice['bottom'])
            temp.append(dice['left'])
            temp.append(dice['top'])
            temp.append(dice['right'])

        elif direction == 2:  # 서쪽 회전
            # left, top, right, bottom 자리에 올 값 순서대로 들어감
            temp.append(dice['top'])
            temp.append(dice['right'])
            temp.append(dice['bottom'])
            temp.append(dice['left'])

        dice['left'] = temp[0]
        dice['top'] = temp[1]
        dice['right'] = temp[2]
        dice['bottom'] = temp[3]

    elif direction == 3 or direction == 4:
        if direction == 3:  # 남쪽 회전
            # up, top, down, bottom 자리에 올 값 순서대로 들어감
            temp.append(dice['bottom'])
            temp.append(dice['up'])
            temp.append(dice['top'])
            temp.append(dice['down'])

        elif direction == 4:  # 북쪽 회전
            # up, top, down, bottom 자리에 올 값 순서대로 들어감
            temp.append(dice['top'])
            temp.append(dice['down'])
            temp.append(dice['bottom'])
            temp.append(dice['up'])

        dice['up'] = temp[0]
        dice['top'] = temp[1]
        dice['down'] = temp[2]
        dice['bottom'] = temp[3]


# 동서남북 회전 테스트
def test_spin_dice():
    from copy import deepcopy

    test_cases = [deepcopy(dice) for _ in range(4)]
    print(test_cases)

    for i in range(len(test_cases)):
        print('test dice: ', test_cases[i])
        spin_dice(dice=test_cases[i], direction=i+1)
        print('after spinning: ', test_cases[i])


print(N, M, K)
print(MAP)

test_spin_dice()
