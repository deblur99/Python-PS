visited = []


def dfs(currentNode: int):
    visited.append(currentNode)
    visited_table[currentNode - 1] = True  # 방문 리스트 갱신
    for node in adjacency_list[currentNode - 1]:
        if not visited_table[node - 1]:  # 현재 노드와 인접한 노드 중 방문하지 않은 노드를 탐색
            dfs(node)


if __name__ == '__main__':
    V, E = list(map(int, input().split()))
    # 인접리스트, 방문테이블 초기화
    global adjacency_list
    global visited_table

    adjacency_list = [[] for _ in range(V)]
    visited_table = [False for _ in range(V)]

    for _ in range(E):
        src, dest = list(map(int, input().split()))
        adjacency_list[src - 1].append(dest)
        adjacency_list[dest - 1].append(dest)

    connect_components = 0
    for node in range(1, V + 1):
        # 이미 탐색한 노드면 탐색 생략
        if visited_table[node - 1]:
            continue

        # 아직 탐색하지 않은 노드면 연결 요소이므로 해당 노드부터 탐색
        visited = []
        dfs(node)
        connect_components += 1
        print(visited)

    print(connect_components)
