a,b,c = list(map(lambda n: int(n), input().split()))
val = 1

# 세 값으로 모두 나누어 떨어지는 값 중 가장 작은 값을 최소공배수라고 부를 수 있다.
while val % a != 0 or val % b != 0 or val % c != 0:
  val += 1

print(val)