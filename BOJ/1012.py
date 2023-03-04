import sys
sys.setrecursionlimit(10**7)    # 이거 안하면 RecursionError 뜸. 재귀호출 최대치 높여줘야 ㅎ마
input = sys.stdin.readline


def dfs(row, col):
    if graph[row][col] == 1:
        graph[row][col] = 2
        if row < N and col + 1 < M and graph[row][col + 1] == 1:
            dfs(row, col + 1)
        # 문제는 오른쪽과 아래쪽만 간다는 것 -> 왼쪽, 위쪽도 뒤져봐야 함
        if row < N and col - 1 > -1 and graph[row][col - 1] == 1:
            dfs(row, col - 1)
        if col < M and row - 1 > -1 and graph[row - 1][col] == 1:
            dfs(row - 1, col)
        if col < M and row + 1 < N and graph[row + 1][col] == 1:
            dfs(row + 1, col)
        return 1
    return 0


answers = []
T = int(input())
for _ in range(T):
    answer = 0
    M, N, K = list(map(int, input().split()))

    graph = [[0 for _ in range(M)] for __ in range(N)]

    for __ in range(K):
        x, y = list(map(int, input().split()))
        graph[y][x] = 1

    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                answer += dfs(y, x)

    answers.append(answer)

# 결과값 여러개면 테케 처리할 때마다 리스트에 넣어두고 한꺼번에 출력
for answer in answers:
    print(answer)


# 반례 (오른쪽, 아래쪽만 가는 case에 십자모양을 넣어보았다)
'''
1
10 10 5
5 5
4 5
5 4
6 5
5 6
'''
# 원래 답: 1
# 실행결과: 2
# -> solution: 위쪽, 왼쪽도 고려하기

'''
5
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
7 7 8
0 0
0 1
1 0
1 2
1 3
1 4
4 5
4 6
7 7 8
0 0
0 1
1 0
1 2
1 3
1 4
4 5
4 6
7 7 8
0 0
0 1
1 0
1 2
1 3
1 4
4 5
4 6
'''

'''
1
5 5 5
0 0
0 1
0 3
0 4
0 2
'''
