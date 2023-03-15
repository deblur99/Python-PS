import sys

input = sys.stdin.readline

answer = 0


def dfs(node, pos):
    if not visited[node -1]:
        pos += 1

        # 중요) 최종적으로 도달한 경우에 대해서만 별도의 변수에 저장한다.
        if node == end:
            global answer
            answer = pos

        visited[node-1] = True
        for next in relatives[node-1]:
            # 각 호출 스택별로 현재 상태값을 따로따로 저장해야 하므로,
            # 이때 함수 매개변수에 상태값을 추가로 저장해주어야 한다.
            # 절대로 최종 변수에 값을 직접적으로 누적해서는 안 된다.
            dfs(next, pos)


n = int(input())
start, end = list(map(int, input().split()))
m = int(input())

relatives = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(m):
    x, y = list(map(int, input().split()))
    relatives[x - 1].append(y)
    relatives[y - 1].append(x)

dfs(start, 0)

print(answer - 1)

