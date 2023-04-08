import sys
input = sys.stdin.readline

graph = []
result = 0

N, M = list(map(int, input().split()))
for i in range(N):
  row = input()
  row_to_graph = []
  for j in range(M):
    row_to_graph.append(int(row[j]))
  graph.append(row_to_graph)
  
visited = [[False for _ in range(M)] for __ in range(N)]


def dfs(row, col):
  if not visited[row][col]:
    visited[row][col] = True
    if row - 1 >= 0 and graph[row-1][col] == 0:
      dfs(row-1, col)
    if col - 1 >= 0 and graph[row][col-1] == 0:
      dfs(row, col-1)
    if row + 1 < N and graph[row+1][col] == 0:
      dfs(row+1, col)
    if col + 1 < M and graph[row][col+1] == 0:
      dfs(row, col+1)
    return True # 찾은 부분에 대해서만 True 반환
  else:
    return False # 찾은 부분이 없다면 False 반환
    
    
for i in range(N):
  for j in range(M):
    if graph[i][j] == 0 and dfs(i, j): # 유효한 그래프를 탐색했을 때만 1 증가시키기 위해 조건문 사용
      result += 1

print(result)
    