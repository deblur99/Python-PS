from random import randint

array = []

while len(array) < 10:
  item = randint(1, 10)
  while item in array:
    item = randint(1, 10)  
  array.append(item)
  
  
print(array)
  
# sorting -> O(NlogN) or O(N^2) (worst case)
def quick_sort(array, start, end):
  if start >= end:
    return
  pivot = start
  left = start+1  # 피벗은 첫 번째 원소, left는 피벗의 그 다음번쨰 원소
  right = end
  while left <= right:
    while left <= end and array[left] <= array[pivot]:
      left += 1
    while right > start and array[right] >= array[pivot]:
      right -= 1
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]
  
  # partition
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)


def quick_sort_simple(array):
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  tail = array[1:]
  
  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort_simple(left_side) + [pivot] + quick_sort_simple(right_side)
  

# quick_sort(array, 0, len(array)-1)  
array = quick_sort_simple(array)
print(array)