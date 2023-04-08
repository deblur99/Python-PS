import sys
input = sys.stdin.readline


def binary_search(array, target, start, end):
  if start > end: # 시작점과 끝점이 역전되는 경우는 존재하지 않음을 나타낸다.
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    # 중간값이 target보다 오른쪽에 있으면, 오른쪽 탐색 범위를 줄인다.
    return binary_search(array, target, start, mid - 1) # mid는 이미 알고 있으므로 그 왼쪽을 끝점으로 하여 탐색 계속함
  else:
    # 중간값이 target보다 왼쪽에 있으면, 왼쪽 탐색 범위를 줄인다.
    return binary_search(array, target, mid + 1, end)
  
n, target = list(map(int, input().rstrip().split()))
array = list(map(int, input().rstrip().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
  print("No result")
else:
  print(result + 1) # 인덱스는 0부터 시작