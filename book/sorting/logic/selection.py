from random import randint

array = []

while len(array) < 10:
  item = randint(1, 10)
  while item in array:
    item = randint(1, 10)  
  array.append(item)
  
  
print(array)
  
# sorting -> O(N^2)
for i in range(len(array)):
  min_idx = i
  for j in range(i+1, len(array)):
    if array[min_idx] > array[j]:
      min_idx = j
  array[i], array[min_idx] = array[min_idx], array[i]
    
print(array)