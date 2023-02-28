# n x n 격자의 정사각형 칸
# 격차에는 인형이 있는 칸이 있고, 없는 칸도 있다.
# 격자의 가장 아래 칸부터 차곡차곡 쌓인다.
# 집어올릴 때는 당연히 각 column의 최상단에 있는 칸부터 접근하며,
# 스택 형태의 바구니에 담긴다.

# 스택에 '연속해서' 쌓이면 두 인형은 스택에서 모두 제거된다.

# 빈 column에서 들어올리려 하면 아무것도 일어나지 않는다.

# moves 값만큼 크레인을 들어올렸을 떄, 연속해서 사라지는 인형의 개수 리턴

from collections import deque


def solution(board, moves):
    answer = 0

    print(board)

    # 판 깔기
    columns = {}
    for i in range(len(board)):
        column = deque()
        for j in range(len(board)):
            if board[j][i] != 0:
                column.append(board[j][i])
        columns[i + 1] = column

    print(columns)

    # 크레인 움직여서 스택에 넣기
    # 연속으로 2개 들어가는 case에 유의한다.
    stack = []
    for idx, move in enumerate(moves):
        print(stack)
        if len(stack) > 0 and stack[-1] == list(columns[move]):
            stack.pop()
            columns[move].popleft()
            answer += 2
            print(answer)
            continue

        if len(columns[move]) > 0:
            stack.append(columns[move][0])
            columns[move].popleft()

    return answer


if __name__ == '__main__':
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))