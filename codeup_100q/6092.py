n = int(input())
call_nums = list(map(lambda n: int(n), input().split()))
total_nums = [0 for i in range(23)]

for call_num in call_nums:
  total_nums[call_num - 1] += 1
  
for total_num in total_nums:
  print(total_num, end=' ')