"""
준비물
1) 인접 리스트 (adjacency list)
2) 방문 테이블 (visit table)
"""

from collections import deque

if __name__ == '__main__':
    with open("my_test_case.txt", "r") as f:
        v_count, e_count = list(map(lambda n: int(n), f.readline().split()))

        adjacency_list = {}
        visit_table = [False for i in range(v_count)]

        for i in range(e_count):
            v_src, v_dest = list(map(lambda n: int(n), f.readline().split()))

            if v_src not in list(adjacency_list.keys()):
                adjacency_list[v_src] = [v_dest]
            else:
                adjacency_list[v_src].append(v_dest)

            if v_dest not in list(adjacency_list.keys()):
                adjacency_list[v_dest] = []

        # run BFS
        visited = []
        queue = deque([1])

        while len(queue) > 0:
            current_node = queue.popleft()

            # 인접 테이블 조회 부분은 꼭 들어가야 한다.
            # 안 그럼 무한루프
            if visit_table[current_node - 1]:
                continue

            visit_table[current_node - 1] = True

            for node in adjacency_list[current_node]:
                queue.append(node)

            visited.append(current_node)

        print(visited, visit_table)