from random import randint
from collections import Counter

array = []

while len(array) < 20:
  item = randint(1, 20)
  array.append(item)
  
counter = Counter(array)

print(array)

# sorting -> O(N + K)
array = []
ks = list(counter.keys())
ks.sort()
for k in ks:
  for _ in range(counter[k]):
    array.append(k)

print(array)