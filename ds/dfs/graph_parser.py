def parse_graph() -> list:
    with open("my_test_case.txt", "r") as f:
        edges = []
        N, M = list(map(lambda n: int(n), f.readline().split()))
        for i in range(M):
            edges.append(tuple(f.readline().split()))

        return len(edges), edges


if __name__ == '__main__':
    print(parse_graph())