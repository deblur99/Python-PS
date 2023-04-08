import sys

input = sys.stdin.readline

from collections import deque

inpt = []

while inpt != [0, 0]:
    result = 0
    inpt = list(map(int, input().split()))
    w, h = inpt

    maze = []
    for _ in range(h):
        inpt = list(map(int, input().split()))
        maze.append(inpt)

    print(maze)  # debug

    # BFS
    visited = [[False for c in range(w)] for r in range(h)]

    for i in range(h):
        for j in range(w):
            if maze[i][j] == 0:
                continue
            else:
                queue = deque([(i, j)])

            while len(queue) > 0:
                print(queue)

                current = queue.popleft()
                print(current)

                if visited[current[0]][current[1]]:
                    continue

                visited[current[0]][current[1]] = True

                # (current[0], current[1]) -> current
                # (current[0] + 1, current[1]) -> down
                # (current[0], current[1] + 1) -> right
                # (current[0] - 1, current[1]) -> up
                # (current[0], current[1] - 1) -> left
                # (current[0] - 1, current[1] - 1) -> up, left
                # (current[0] - 1, current[1] + 1) -> up, right
                # (current[0] + 1, current[1] - 1) -> down, left
                # (current[0] + 1, current[1] + 1) -> down, right
                # TODO: 조건식 달기
                if current[0] + 1 < h and maze[current[0] + 1][current[1]] == 1 and not visited[current[0] + 1][current[1]]:
                    queue.append((current[0] + 1, current[1]))
                if current[1] + 1 < w and maze[current[0]][current[1] + 1] == 1 and not visited[current[0]][current[1] + 1]:
                    queue.append((current[0], current[1] + 1))
                if current[0] - 1 >= 0 and maze[current[0] - 1][current[1]] == 1 and not visited[current[0] - 1][current[1]]:
                    queue.append((current[0] - 1, current[1]))
                if current[1] - 1 >= 0 and maze[current[0]][current[1] - 1] == 1 and not visited[current[0]][current[1] - 1]:
                    queue.append((current[0], current[1] - 1))
                if current[0] - 1 >= 0 and current[1] - 1 >= 0 and maze[current[0] - 1][current[1] - 1] == 1 and not visited[current[0] - 1][current[1] - 1]:
                    queue.append((current[0] - 1, current[1] - 1))
                if current[0] - 1 >= 0 and current[1] + 1 < w and maze[current[0] - 1][current[1] + 1] == 1 and not visited[current[0] - 1][current[1] + 1]:
                    queue.append((current[0] - 1, current[1] + 1))
                if current[0] + 1 < h and current[1] - 1 >= 0 and maze[current[0] + 1][current[1] - 1] == 1 and not visited[current[0] + 1][current[1] - 1]:
                    queue.append((current[0] + 1, current[1] - 1))
                if current[0] + 1 < h and current[1] + 1 < w and maze[current[0] + 1][current[1] + 1] == 1 and not visited[current[0] + 1][current[1] + 1]:
                    queue.append((current[0] + 1, current[1] + 1))

            result += 1

    print(result)