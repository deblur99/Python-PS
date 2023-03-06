import sys

input = sys.stdin.readline

from collections import deque


def dfs(node):
    if not visited_table[node-1]:
        visited_table[node-1] = True
        result[0].append(node)
        for adjacent_node in adjacency_list[node-1]:
            dfs(adjacent_node)

    # (다른 방법)
    # visited_table[node - 1] = True  # 방문테이블 수정하고
    # result[0].append(node)
    # for adjacent_node in adjacency_list[node - 1]:
    #     if not visited_table[adjacent_node - 1]:
    #         dfs(adjacent_node)  # 인접한 노드 중 방문하지 않은 노드를 탐색


N, M, V = list(map(int, input().split()))
adjacency_list = [[] for _ in range(N)]
visited_table = [False for _ in range(N)]

for _ in range(M):
    src, dest = list(map(int, input().split()))
    adjacency_list[src - 1].append(dest)
    adjacency_list[dest - 1].append(src)

result = [[], []]  # 각각 DFS, BFS 수행결과. 요소는 List<int>

# 인접리스트를 오름차순으로 정렬
for i in range(len(adjacency_list)):
    adjacency_list[i].sort()

dfs(V)

# bfs
queue = deque([V])  # 자료구조 초기화
visited_table = [False for _ in range(N)]  # 방문테이블 초기화

while len(queue) > 0:
    current_node = queue.popleft()  # 큐에서 하나 꺼내고
    if not visited_table[current_node - 1]:  # 방문테이블 방문여부 검사하고
        visited_table[current_node - 1] = True  # 방문테이블 True로 표시하고
        result[1].append(current_node)
        for adjacent_node in adjacency_list[current_node - 1]:
            queue.append(adjacent_node)  # 인접테이블 조회해서 인접한 노드들 큐에 추가

# 결과값 출력
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=' ')
    print()
