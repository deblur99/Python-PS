till = int(input())
sum = 0

for i in range(1, till+1):
    sum += i
    if (sum >= till):
      break

print(sum)