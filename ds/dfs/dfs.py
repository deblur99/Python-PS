import random


def generate_test_case():
    N = random.randint(1, 10)
    M = random.randint(0, N * (N - 1) / 2)

    edges = []

    # for i in range(M):
    while len(edges) != M:
        u = random.randint(1, N)
        v = random.randint(1, N)
        while v == u:
            v = random.randint(1, N)

        if (u, v) in edges:
            continue
        else:
            edges.append((u, v))

    with open('my_test_case.txt', 'w') as f:
        f.write(f"{N} {M}\n")
        for edge in edges:
            f.write(f"{edge[0]} {edge[-1]}\n")

    print('writing completed')  # debug


if __name__ == '__main__':
    # vertex, edge 개수
    N, M = list(map(lambda n: int(n), input().split()))

    # 구현해야 할 것
    # - 인접 리스트
    # - 방문 리스트
    adjacent_list = {}
    visit_list = [False for i in range(N)]

    # edge의 양 끝점 u, v
    for i in range(M):
        u, v = list(map(lambda n: int(n), input().split()))

        if u not in list(adjacent_list.keys()):
            adjacent_list[u] = [v]
        else:
            adjacent_list[u].append(v)

    print(adjacent_list)
    print(visit_list)

    generate_test_case()
