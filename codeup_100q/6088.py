# input 기본 형태
# split()의 인자에 ' ' delimeter를 적지 않아도 공백 기준으로 점검한다.
# 따라서, split(' ') 대신 split()을 써서 불필요한 오답을 방지
a,d,n = list(map(lambda n: int(n), input().split()))
result = a

for i in range(1, n):
  result += d

print(result)