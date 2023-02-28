# 큐는 FIFO (First In First Out)
# 1. 큐는 front과 rear로 이루어져 있다. 결론만 말하면, 데이터는 rear에서 삽입되어 front에서 삭제된다.
# 2. rear: 데이터가 삽입되는 위치 (enqueue)
# 3. front: 데이터가 삭제되는 위치 (dequeue)

# 파이썬에서의 큐 연산자
# 1. append : enqueue 연산으로, rear에 데이터를 삽입한다.
# 2. popleft : dequeue 연산으로, front에 있는 데이터를 삭제한다. 
# (rear와 반대 방향의 위치이므로 pop이 아닌 popleft)

# 큐 가져오기
from collections import deque

# 큐 객체 생성하기
queue = deque()

queue.append(10)
queue.append(20) 
queue.append(30)  # queue에 요소가 삽입될수록, rear의 요소만 바뀐다.
queue.append(40)
queue.append(50)
print(queue)

# queue에 요소가 제거되면, front에 있는 요소가 제거되고
# 그 뒤에 있는 요소가 front에 있는 요소가 된다.
queue.popleft() 
print(queue)

# 파이썬의 deque은 0번 인덱스가 front, -1번 인덱스가 rear로 꽤 직관적인 구성을 보여준다.
queue.popleft() 
print(queue)

queue.popleft() 
print(queue)

queue.popleft() 
print(queue)

queue.append(100)
print(queue)

queue.append(200)
print(queue)