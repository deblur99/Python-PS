n = int(input())
call_nums = list(map(lambda n: int(n), input().split()))  

for call_num in reversed(call_nums):
  print(call_num, end=' ')