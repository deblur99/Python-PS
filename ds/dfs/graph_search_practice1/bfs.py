from collections import deque

if __name__ == '__main__':
    V, E = list(map(int, input().split()))
    adjacency_list = [[] for _ in range(V)]
    visited_list = [False for _ in range(V)]

    for _ in range(E):
        src, dest = list(map(int, input().split()))
        adjacency_list[src - 1].append(dest)
        adjacency_list[dest - 1].append(src)

    connect_components = 0
    queue = deque()  # 시작 노드를 큐에 넣는 것으로 시작

    for node in range(1, V + 1):
        if visited_list[node - 1]:
            continue

        visited = []

        queue.clear()
        queue.append(node)

        while len(queue) > 0:
            current_node = queue.popleft()
            if not visited_list[current_node - 1]:
                visited.append(current_node)
                visited_list[current_node - 1] = True
                for adjacency_node in adjacency_list[current_node - 1]:
                    queue.append(adjacency_node)

        connect_components += 1
        print(visited)

    print(connect_components)
