# 준비물 (DFS, BFS 공통)

vertices = (vertex 개수)

- 인접리스트 (from 그래프)
    - adjacencyList<Vertex<List<Vertex>>>(vertices)
- 방문리스트
    - visitedList<bool>(vertices)

- 1번
    - dfs
      [1, 2, 5]
      [3, 4, 6]
      2

    - bfs
      [1, 2, 5]
      [3, 4, 6]
      2

- 2번
    - 그래프
      6 8
      1 2
      2 5
      5 1
      3 4
      4 6
      5 4
      2 4
      2 3
    - dfs
      [1, 2, 5, 4, 6, 3]
      1
    - bfs
      [1, 2, 5, 4, 3, 6]
      1