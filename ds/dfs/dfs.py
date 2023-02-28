from graph_generator import generate_test_case
from graph_parser import parse_graph


# Remark: DFS, BFS의 준비물
# - 인접 리스트 (dict)
# - 방문 테이블 (list)
# - 각 탐색에 맞게 구현한다.
def dfs_in_array(adjacent_list: dict, visit_list: list) -> (int, list):
    visited = []
    root = 1

    stack = [root]  # 스택을 root 노드만 들어가 있는 상태로 초기화하여 탐색 시작
    while len(stack) > 0:
        # 1) 스택의 최상단에 있는 노드를 꺼낸다.
        current_node = stack.pop()

        # 1-1) 꺼낸 노드를 방문 리스트에 참조하여, 해당 노드가 True라면 건너뛴다.
        if visit_list[current_node-1]:
            continue

        # 2) 꺼낸 노드로 인접 리스트를 참조하고, 그 노드에 해당하는 리스트를 가져온다.
        # 리스트에 있는 요소들을 앞에서부터 차례대로 스택에 저장한다.
        for node in adjacent_list[current_node]:
            stack.append(node)

        # 3) 꺼낸 노드를 방문 테이블에 반영한다. (False -> True로)
        visit_list[current_node-1] = True   # 인덱스에 유의!

        # 4) 그래프 순회하면서 필요한 작업이 따로 있다면 그것도 같이 수행한다.
        visited.append(current_node)

        # 사실 순서는 2번 먼저 해도, 3번 먼저 해도, 또는 4번 먼저 해도 상관은 없다!
        # 다만, 1번은 다른 과정보다 먼저 해야 한다.
        print(visited, visit_list)

    # 문제에서는 순회한 노드의 목록을 반환하여야 하므로 visited를 반환한다.
    return len(visited), visited


generate_graph = False

if __name__ == '__main__':
    if generate_graph:
        generate_test_case()

    # vertex, edge 개수
    with open("my_test_case.txt", "r") as f:
        N, M = list(map(lambda n: int(n), f.readline().split()))

        # 구현해야 할 것
        # - 인접 리스트
        # - 방문 리스트
        adjacent_list = {}
        visit_list = [False for i in range(N)]

        # edge의 양 끝점 u, v
        for i in range(M):
            u, v = list(map(lambda n: int(n), f.readline().split()))

            if u not in list(adjacent_list.keys()):
                adjacent_list[u] = [v]
            else:
                adjacent_list[u].append(v)

            if v not in list(adjacent_list.keys()):
                adjacent_list[v] = []

        print(adjacent_list)
        print(visit_list)

        # 구현한 것을 적용하여 그래프 탐색
        count, result = dfs_in_array(adjacent_list, visit_list)
        print(result)


