import sys
input = sys.stdin.readline

N = int(input())
N_arr = list(map(int, input().split()))
N_arr.sort()

M = int(input())
M_arr = list(map(int, input().rstrip().split()))

def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if N_arr[mid] == target:
    return mid
  elif N_arr[mid] > target:
    return binary_search(array, target, start, mid - 1)
  elif N_arr[mid] < target:
    return binary_search(array, target, mid + 1, end)
  
result = []  
for target in M_arr:
  if binary_search(N_arr, target, 0, N-1) is None:
    result.append('no')
  else:
    result.append('yes')
    
print(result)

# set()를 써서 존재 여부를 확인하며 풀어도 된다. 그리고 이게 더 pythonic한 풀이 방법이다.