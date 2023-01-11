call_count = int(input())
call_list = list(map(lambda n: int(n), input().split()))
min = call_list[0]

for num in call_list:
  if min > num:
    min = num

print(min)