'''
세로는 무조건 길이가 2로 고정
가로 2, 세로 1인 직사각형으로 채우는 경우의 수를 리턴
'''
from itertools import combinations


def solution(n):
    answer = 0

    portrait = [2, 1]
    landscape = [1, 2]

    target = [2, n]

    # 1) 가로 길이를 위주로 접근하기?
    for n in range(5, 21):

        for try_landscapes in range(0, n // 2 + 1):
            try_portraits = 0

            if n - try_landscapes * 2 > 0:
                try_portraits = n - try_landscapes * 2

            print(try_portraits, try_landscapes)
            print(len(combinations(try_portraits + 1, try_landscapes)))

        print()

    # 홀수 1, 3, 5, ... -> 가로 (남은 길이 // 2) + 세로 하나
    #   -> 아니면 가로 개수 줄어든만큼 세로를 늘리거나
    # 짝수 2, 4, 6, ... -> 가로만 놓거나 세로만 놓거나
    #   -> 마찬가지로 가로 개수 줄어든만큼 세로를 늘리거나
    # 나머지는 가로, 세로 조합의 위치 조정

    return answer


if __name__ == '__main__':
    solution(10)
