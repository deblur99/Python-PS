# 문제는 같은 촌수!
# 같은 촌수들부터 먼저 탐색하고 그 다음 촌수를 탐색해야 한다.
# 따라서, DFS가 아니라 BFS를 써서 탐색해야 한다. -> ㄴㄴ

import sys

input = sys.stdin.readline

from collections import deque

answer = 0


def BFS():
    global answer

    queue = deque([start])

    while len(queue) > 0:
        current_node = queue.popleft()

        if not visited[current_node - 1]:
            print(current_node)
            visited[current_node - 1] = True
            answer += 1
            for next_node in relatives[current_node - 1]:
                if next_node == end:
                    visited[next_node - 1] = True
                    return
                queue.append(next_node)



n = int(input())
start, end = list(map(int, input().split()))
m = int(input())

relatives = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(m):
    x, y = list(map(int, input().split()))
    relatives[x - 1].append(y)
    relatives[y - 1].append(x)

BFS()

if not visited[end - 1]:
    print(-1)
else:
    print(answer)
