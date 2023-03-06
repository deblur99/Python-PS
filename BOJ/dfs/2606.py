# 굉장히 정석적인 풀이방법
# 1. 그래프를 입력받는다.
# 2. 인접리스트와 방문테이블을 초기화한다.
# 3. 탐색한다.
# * 방향 여부, 그래프 끊어짐 여부에 유의한다.
import sys

input = sys.stdin.readline

global answer
answer = 0


def dfs(node):
    global answer
    if not visited_table[node - 1]:
        if node != 1:
            answer += 1
        visited_table[node - 1] = True
        for next in adjacency_list[node - 1]:
            dfs(next)


V = int(input())
E = int(input())
adjacency_list = [[] for _ in range(V)]
visited_table = [False for _ in range(V)]

for _ in range(E):
    src, dest = list(map(int, input().split()))
    adjacency_list[src - 1].append(dest)
    adjacency_list[dest - 1].append(src)

dfs(1)
print(answer)
