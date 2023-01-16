T = int(input())
numbers = list()
table = dict()

for i in range(T):
  number = int(input())
  if number not in list(table.keys()):
    table[number] = 1
  else:
    table[number] += 1

count = 0
for number in list(table.keys()):
  if (table[number] == 2):
    count += 1
    
print(count)
