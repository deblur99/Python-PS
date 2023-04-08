import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

graph = []
visited = [[False for _ in range(M)] for __ in range(N)]

for i in range(N):
  row = input()
  row_to_graph = []
  for j in range(M):
    row_to_graph.append(int(row[j]))
  graph.append(row_to_graph)
  
results = []

def dfs(row, col, moves=0):
  if row == N - 1 and col == M - 1:
    global results
    results.append(moves)
  
  if not visited[row][col]:
    visited[row][col] = True
    if row - 1 >= 0 and graph[row-1][col] == 1:
      dfs(row-1, col, moves+1)
    if row + 1 < N and graph[row+1][col] == 1:
      dfs(row+1, col, moves+1)
    if col + 1 < M and graph[row][col+1] == 1:
      dfs(row, col+1, moves+1)
  
dfs(0,0)
results.sort()
print(results[0]+1) # 시작 칸 포함해서 이동 거리를 계산해야 하므로 1 더해야 한다.
    