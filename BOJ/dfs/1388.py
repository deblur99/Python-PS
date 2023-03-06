# 1 직관적으로 풀기 (빡구현...)
def solution():
    row, col = list(map(int, input().split()))
    maze = ['' for __ in range(row)]

    for i in range(row):
        maze[i] = input()

    result = 0

    # 순서대로 찾기
    # | -> stack에 인덱스대로 저장
    # - -> 이어지다가 끊어지면 +1

    # - 찾기
    for i in range(row):
        last = maze[i][0]
        for j in range(col):
            if last == '-' and maze[i][j] == '-':
                continue

            if last == '-' and maze[i][j] == '|':
                last = '|'
                result += 1

            if last == '|' and maze[i][j] == '-':
                last = '-'

        if last == '-':
            result += 1

    table = [False for _ in range(col)]

    for i in range(row):
        for j in range(col):
            if maze[i][j] == '|':
                if not table[j]:
                    table[j] = True

            else:
                if table[j]:
                    result += 1
                    table[j] = False

        if i == row - 1:
            for j in table:
                if j:
                    result += 1

    print(result)


if __name__ == '__main__':
    solution()