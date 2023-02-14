def solution(numbers, hand):
    answer = ''

    # 1) 버튼~왼쪽 거리, 버튼~오른쪽 거리 각각 구하고
    # 2) 둘 중에 작은 쪽 엄지를 사용한다.
    # 2-1) 같다면 왼손잡이, 오른손잡이 따라 가고
    # 3) 누른 쪽 위치를 업데이트한다.
    def get_decision(dest: int, left: tuple, right: tuple) -> str:
        ROW = 0
        COL = 1

        left_distance = abs(num_pos[dest][ROW] - left[ROW]) + abs(num_pos[dest][COL] - left[COL])

        right_distance = abs(num_pos[dest][ROW] - right[ROW]) + abs(num_pos[dest][COL] - right[COL])

        if left_distance < right_distance:
            finger_pos['left'] = num_pos[dest]
            return 'L'
        elif right_distance < left_distance:
            finger_pos['right'] = num_pos[dest]
            return 'R'
        else:
            finger_pos[hand] = num_pos[dest]
            return hand[0].upper()  # return L or R

    # 시작 위치
    # 왼손 엄지는 *, 오른손 엄지는 #
    # 엄지는 상하좌우 4가지 방향으로 이동 가능하고, 이동거리는 한 칸당 1
    # 왼쪽 열의 3개 숫자 1, 4, 7 입력할 때에는 왼손 엄지 사용
    # 오른쪽 열의 3개 숫자 3, 6, 9 입력할 떄에는 오른쪽 엄지 사용
    # 가운데 열의 4개 숫자 2, 5, 8, 0 입력할 때에는 두 엄지 손가락의 현재 키패드의 위치
    # 에서 더 가까운 엄지 사용
    # -> 양쪽 엄지의 거리가 같다면, 왼손잡이는 왼쪽을, 오른손잡이는 오른쪽을 이용한다.
    num_pos = {
        '1': (0, 0),
        '2': (0, 1),
        '3': (0, 2),

        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),

        '7': (2, 0),
        '8': (2, 1),
        '9': (2, 2),

        '*': (3, 0),
        '0': (3, 1),
        '#': (3, 2)
    }

    # init finger_pos
    finger_pos = {
        'left': num_pos['*'],
        'right': num_pos['#']
    }

    # dest: 눌러야 할 키패드의 번호
    # left: 이전 시점의 왼손 키패드 좌표
    # right: 이전 시점의 오른손 키패드 좌표
    numbers = list(map(lambda n: str(n), numbers))

    for num in numbers:
        if num in ['1', '4', '7']:
            answer += 'L'
            finger_pos['left'] = num_pos[num]
        elif num in ['3', '6', '9']:
            answer += 'R'
            finger_pos['right'] = num_pos[num]
        elif num in ['2', '5', '8', '0']:
            answer += get_decision(num, finger_pos['left'], finger_pos['right'])

    return answer


def test():
    cases = [
        [
            [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],
            "right",
            "LRLLLRLLRRL"
        ],
        [
            [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],
            "left",
            "LRLLRRLLLRR"
        ],
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            "right",
            "LLRLLRLLRL"
        ]
    ]

    for idx, case in enumerate(cases):
        if case[-1] == solution(case[0], case[1]):
            print(f"passed case {idx}")


if __name__ == '__main__':
    test()