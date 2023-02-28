# i~j 자르고 정렬 -> k번째 수 리턴 (i, j는 1부터 시작한다.)

def solution(array, commands):
    answer = []

    for command in commands:
        subarray = array[command[0]:command[1] + 1]
        subarray.sort()
        answer.append(subarray[command[2]])

    return answer


if __name__ == '__main__':
    solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])