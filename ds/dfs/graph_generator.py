import random


def generate_test_case(v_count: int):
    if v_count < 1:
        return

    N = random.randint(1, v_count)
    M = random.randint(0, N * (N - 1) / 2)

    edges = []

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
