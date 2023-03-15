import sys

input = sys.stdin.readline

global answer
answer = 0


def DFS(node, prev, target):
    global answer

    if not visited[node - 1]:
        if prev > -1 and not added[prev] and node != start:
            answer += 1
            added[prev] = True

        visited[node - 1] = True
        # 자기 자신은 0촌이다.
        # 즉, 출발 노드부터 카운팅하면 안 된다.
        # print(node)

        for child in relatives[node - 1]:
            DFS(child, node, target)


# 두 node 사이의 거리를 계산
n = int(input())
start, end = list(map(int, input().split()))
m = int(input())

relatives = [[] for _ in range(n)]
visited = [False for _ in range(n)]

added = [False for _ in range(n)]  # 이미 더했는지 여부 확인

for _ in range(m):
    # x는 y의 부모 번호 (x -> y directed. 반대 방향은 없음)
    # 반대 방향은 없는 줄 알았으나.. 역으로 거슬러 올라가는 경우도 고려해야 함
    # 따라서 undirected
    x, y = list(map(int, input().split()))
    relatives[x - 1].append(y)
    relatives[y - 1].append(x)

if start == end:
    print(0)
else:
    DFS(start, -1, end)
    if not visited[end - 1]:
        print(-1)
    else:
        print(answer)
