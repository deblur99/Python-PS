# 2 DFS 구현하여 풀이 (다른 사람 풀이)

# 입출력 최적화 -> BOJ, 삼성 등등 이렇게 써야 함
import sys
input = sys.stdin.readline


def dfs(row, col):
    # - case
    if graph[row][col] == '-' and col+1 < M and graph[row][col+1] == '-':
        dfs(row, col+1)

    # | case 로 나누어 탐색
    if graph[row][col] == '|' and row+1 < N and graph[row+1][col] == '|':
        dfs(row+1, col)

    # 이미 탐색한 부분은 .로 바꿈
    graph[row][col] = '.'
    return 1


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    graph = [list(input().strip()) for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] != '.':
                answer += dfs(i, j)

    print(answer)