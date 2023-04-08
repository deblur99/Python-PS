# 이진탐색의 핵심
# 조건 - 탐색하려는 배열이 정렬되어 있어야 한다.
# 0. start와 end의 자리가 역전 -> 검색 실패
# 1. mid == target
#   return mid
# 2. mid > target
#   end <- mid - 1
# 3. mid < target
#   start <- mid + 1
# 중간값 새로 정하기 -> (start + end) // 2

# 시간복잡도는 O(logN)이다.
# 자주 써먹을 데가 많으니 잘 알아두자.

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result is not None:
  print(result+1)