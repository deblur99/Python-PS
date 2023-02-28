# DFS 메서드 정의
# 필요한 것
# 1) graph : 인접 행렬 또는 인접 리스트 형태
# 2) v : 최초 탐색하는 노드 (BST의 경우 0)
# 3) visited : 노드 개수만큼의 크기를 가지며, 기본적으로 False로 초기화되어 있는 방문 여부 확인 리스트

def DFS(graph: list, v: int, visited: list):
  # 현재 노드를 방문처리
  visited[v] = True
  print(v, end=' ')
  
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      DFS(graph, i, visited)
      

graph: list = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited: list = [False for _ in range(9)]

# 정의된 DFS 메서드 호출
DFS(graph, 1, visited)