'''
1 이닝 -> 공격, 수비 1회씩
총 N이닝 만큼 진행

한 이닝에 3아웃이 발생하면 이닝이 종료
두 팀이 공격과 수비를 바꾼다

두 팀은 경기가 시작하기 전까지 타순을 정한다.
1번 타자가 다시 타석에 선다
타순은 이닝이 변경돼도 순서를 유지한다
2이닝에 6번 타자가 마지막이면, 3이닝은 7번타자부터 (리셋 X)
-> 1~9번 타자가 있는데 이닝과 무관하게 순서는 계속 진행되고, 9번까지 했으면 1번부터 다시 시작

공격 팀 선수가 1~3루를 거쳐서 홈에 도착하면 1점 득점
타자가 1~3루 중 하나에 머물 수 있는데, 이 상태의 타자를 주자라고 한다.
이닝이 시작할 때는 주자가 없음

타자가 공을 쳐서 얻을 수 있는 결과는 안타, 2루타, 3루타, 홈런, 아웃
- 안타: 타자와 모든 주자가 1루씩 진루
- 2루타: 타자와 모든 주자가 2루씩 진루
- 3루타: 타자와 모든 주자가 3루씩 진루
- 홈런: 타자와 모든 주자가 홈까지 진루
- 아웃: 모든 주자가 진루하지 못하고, 공격 팀에 아웃 하나 증가

- 초기 조건: 1번 선수 -> 4번 타자. 다른 타자를 결정해야 함
- 가장 많은 득점을 하는 타순을 찾고, 그 득점을 구하자.
'''
import sys

input = sys.stdin.readline


class Inning:
    def __init__(self):
        self.inning = -1

    def get_inning(self):
        return self.inning

    def increment(self):
        self.inning += 1
        return self.inning

    def reset(self):
        self.inning = 0


class Base:
    def __init__(self):
        self.base = 0

    def get_base(self):
        return self.base

    def add(self, count):
        self.base += count
        if self.base > 3:
            self.base = 0  # 모든 루를 돌면 0으로 고정
            return True  # 모든 루를 돌았으면 1점 획득하도록 True 반환
        return False

    def reset(self):
        self.base = 0


class Out:
    def __init__(self):
        self.out = 0

    def get_out(self):
        return self.out

    def increment(self):
        self.out += 1
        if self.out == 3:
            self.out = 0  # 3아웃을 기록하면 이닝이 종료되고 0으로 리셋
            return True  # 아웃 시에는 이닝이 종료되고, 이닝이 종료되었음을 의미하는 True 반환
        return False  # 이닝이 종료되지 않음을 의미하는 false 반환

    def reset(self):
        self.out = 0


class Hitter:
    def __init__(self, origin_list: list):
        self.current_number: int = 0  # init
        self.origin_list: list = origin_list

    def get_number(self):
        return self.origin_list[self.current_number] - 1

    def update_number(self, number):
        if 0 < number < 10:
            self.current_number = number

    def increment_number(self):
        self.current_number += 1
        if self.current_number > 8:
            self.current_number = 0

    def reset(self):
        self.current_number = 0


# 이닝 수
N = int(input())

# 안타 - 1
# 2루타 - 2
# 3루타 - 3
# 홈런 - 4
# 아웃 - 0
innings = []
for i in range(N):
    innings.append(list(map(int, input().split())))

# 최적해가 나올 수 있도록 1번 선수 -> 4번 타자를 제외한 나머지 선수를 배치해야 함
# 한 번 정해지면 그대로 간다.

# 1) 배열 전체를 순회해서 숫자 합이 제일 큰 순서를 내림차순으로 순서 정하기
val_table = {}

for i in range(1, 10):
    val_table[i] = 0
del val_table[4]

for i in range(len(innings)):
    for j in range(len(innings[i])):
        if j != 4 - 1:
            val_table[j + 1] += innings[i][j]

val_table = sorted(val_table.items(), key=lambda item: item[1], reverse=True)
idx_table = list(dict(val_table).keys())
idx_table = idx_table[:3] + [4] + idx_table[3:]

print(idx_table)

inning = Inning()
base = Base()
out = Out()
hitter = Hitter(origin_list=idx_table)

# 이닝 거치면서 지금 몇 번 타자까지 왔는지 체크하며 진행한다.
# 인덱스 순회하는 건 똑같음

# 4번 타자가 1번인 건 고정이고, 나머지는 내가 정해야 함
# 근데 타자 배치하기 전에, 사이클이 의도한대로 잘 돌아가는지 봐야 함

score = 0
while inning.increment() < N:
    while out.get_out() < 3:
        # 타자가 아웃하는 경우 -> 아웃 하나 올리기
        if innings[inning.get_inning()][hitter.get_number()] == 0:
            # 이닝이 종료되어 현재 타자 그 다음 순번의 타자를 다음 타자로 지정
            # 그리고, 다음 이닝으로 넘어간다
            if out.increment():
                hitter.reset()
                break

        # 안타~홈런까지 (1~4)인 경우 현재 상황 업데이트
        if base.add(innings[inning.get_inning()][hitter.get_number()]):
            print(innings[inning.get_inning()][hitter.get_number()])
            score += 1

        hitter.increment_number()

print(score)
