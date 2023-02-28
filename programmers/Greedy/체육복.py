'''
1. 체격순, 바로 앞번호나 뒷번호 학생에게만 빌려줄 수 있다.
2. 최대한 많이 빌려줘야 한다.
* 전체 학생수 n, 분실자 lost, 여유분 reserve
* 최댓값 return
** lost, reserve 기준 같은 숫자가 있는지 확인해야 한다. (이 경우 생략)
'''


def solution(n, lost, reserve):
    new_lost = []

    for i in range(len(lost)):
        if lost[i] not in reserve[i]:
            new_lost.append(lost[i])

    answer = n - len(new_lost)  # init, minimum

    # 인풋으로 주어진 두 배열이 정렬되어 있지 않을 수 있음에 유의해야 한다.
    new_lost.sort()
    reserve.sort()

    # 이번에는 빌려주는 쪽인 reserve를 기준으로 판단해보자 -> 역발상
    for i in range(len(reserve)):
        # 1. reserve 내 요소가 lost에 있을 경우 -> 못 빌려줌 -> 패스
        # ** 앞에서 이미 함
        # if reserve[i] in lost:
        #     lost.remove(reserve[i])
        #     answer += 1

        # 2. reserve의 요소-1 값이 lost에 있을 경우 -> 빌려줌
        # lost에서와 달리 reserve에서는 고려할 필요가 없다? 안됨
        if reserve[i] - 1 in lost:
            new_lost.remove(reserve[i] - 1)
            answer += 1

        elif reserve[i] + 1 in lost:
            new_lost.remove(reserve[i] + 1)
            answer += 1

    # 결과: 5, 8, 18, 20, 24 통과 실패
    # 정렬해주고 나니 5, 24 통과 실패
    # lost에 있는 요소와 reserve에 있는 요소가 같을 수 있는 경우를 고려
    # 이 경우에는? -> 앞에서 해당되는 요소들 제외한 요소들을 새 리스트에 담는다.

    return answer


if __name__ == '__main__':
    solution(5, [2, 4], [1, 3, 5])
