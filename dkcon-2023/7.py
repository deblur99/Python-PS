N, A, B = list(map(lambda n: int(n), input().split()))

table = [[] for i in range(6)]
  
for i in range(6):
  new_table = []
  
  number = int(input())
  for row in range(A):
    table[i].append(list(map(lambda n: int(n), input().split())))
    
  for item in table[i]:
    new_table.extend(item)
    
  table[i] = new_table


'''
번호가 0이면 없는 자리고
0이 아니면 학생 번호

자리에 학생이 있으면 첫 번째 출석 때 표시한 숫자 (테이블에 들어간 숫자)
없으면 0으로 표시

첫 출석에 답하지 않은 학생 (1에서 0번 처리) 
-> 두 번째에 확인되면 첫 출석 체크 때 불렸던 가장 마지막 번호의 그 다음 번호를 지정

첫 출석만 안 하면 지각
첫 번째부터 여섯 번째까지 2번 이상 없으면 결석 처리

먼저 앉아있는 학생이 자리를 비우면 지각한 학생이 앉을 수 있고

수업을 듣는 학생끼리 자리비울 수 없음
'''

# 0 - 부재, 2 - 2번 출석, -1 - 지각
status = [0 for i in range(N)]
late = -1 # 마지막 출석 번호

print(table)

# 첫 번째 출석 처리
for i in range(len(table)):
  for j in range(len(table[i])):

    # 첫 번째 출석
    if i == 0:
      late = max(table[i]) + 1
      if table[i][j] != 0:
        status[table[i][j]] += 1
      
    elif i == 1:
      if table[i][j] != 0:
        if status[table[i][j]] == 0:
          status[table[i][j]] = -1
        if status[table[i][j]] == 0
        
    
    
      
    
    # 두 번째 출석
    # if row == 1:
    #   if status[col-1] == 
     
        
    
      

# 2번째 출석 처리
table[1]

# 3번째 출석 처리
table[2]

# 첫 번째 출석 처리
table[3]

# 첫 번째 출석 처리
table[4]

# 첫 번째 출석 처리
table[5]