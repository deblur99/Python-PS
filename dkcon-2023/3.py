n = int(input())
score_list = list(map(lambda n: int(n), input().split()))
grade_list = list()

for i in range(len(score_list)):
  high = 100
  low = 95
  added_grade = 4.5
  while not (score_list[i] <= high and score_list[i] >= low):
    if (score_list[i] <= 59):
      added_grade = 0
      break    
    added_grade -= 0.5
    high -= 5
    low -= 5
  grade_list.append(3*added_grade)

sum = 0
for grade in grade_list:
  sum += grade
  
print(f'{sum/(3*n):.2f}')