from copy import deepcopy

N = int(input()) # 게임에 참여한 사람 수 
value_list = {
  'bani': 0,
  'dangun': 0,
}
table = list()
for i in range(N):
  table.append(deepcopy(value_list))
  
T = int(input()) # 턴이 넘어가는 횟수
for i in range(T+1):
  if i == 0:
    table[0]['bani'] += 1
    table[0]['bani'] += 1
    continue
  
  target = int(input()) - 1
  prev = target-1
  next = target+1
  
  if prev < 0:
    prev = N-1
  
  if next >= N:
    next = 0
    
  table[target]['bani'] += 1
  table[target]['bani'] += 1
  table[prev]['dangun'] += 1
  table[next]['dangun'] += 1    
    
for i in range(N):
  print(f"{table[i]['bani']} {table[i]['dangun']}")