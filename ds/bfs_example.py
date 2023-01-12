from collections import deque

# BFS 메서드 정의
def BFS(graph: list, start: int, visited: list):
  # 큐 구현을 위해 deque 메서드 사용
  queue = deque([start])
  
  # 현재 노드를 방문 처리
  visited[start] = True
  
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 요소 하나를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')
    
    # 뽑은 요소를 방문 처리
    visited[v] = True
    
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True # 큐에 넣으면서 방문 처리
        

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
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
visited = [False for _ in range(9)]

# 정의된 BFS 함수 호출
BFS(graph, 1, visited)
  