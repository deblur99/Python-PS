from random import randint

array = []

while len(array) < 10:
  item = randint(1, 10)
  while item in array:
    item = randint(1, 10)  
  array.append(item)
  
  
print(array)
  
# sorting -> O(N^2)
for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break
    
print(array)