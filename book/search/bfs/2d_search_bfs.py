from collections import deque

graph = [
  [1, 3],
  [0, 2, 4],
  [1, 5],
  [0, 4, 6],
  [1, 3, 5, 7],
  [2, 4, 8],
  [3, 7],
  [4, 6, 8],
  [5, 7]
]

visited = [False for _ in range(9)]

result = []

def bfs(pos: int):
  queue = deque([pos])

  while len(queue) > 0:
    curr = queue.popleft()
    if not visited[curr]:
      visited[curr] = True      
      result.append(curr)
      for adj in graph[curr]:
        queue.append(adj)
      
bfs(0)

print(result)