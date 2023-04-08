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

def dfs(pos: int):
  if not visited[pos]:
    result.append(pos)
    visited[pos] = True
    for adj in graph[pos]:
      dfs(adj)
      
dfs(0)

print(result)