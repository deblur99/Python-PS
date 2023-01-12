More: https://deblur-log.vercel.app/26e49b3a587045efbe7e3c44df42ad42

# 스택은 LIFO (Last In First Out)

-   스택은 마지막에 삽입된 요소를 top으로 관리한다. top으로 삽입되고 top으로 삭제된다.

# 파이썬에서의 스택 연산자 -> 파이썬에서는 -1번 인덱스가 top으로 간주된다.

1. append : top에 데이터를 삽입한다.
2. pop : top에 있는 데이터를 삭제한다.

# 큐는 FIFO (First In First Out)

1. 큐는 front과 rear로 이루어져 있다. 결론만 말하면, 데이터는 rear에서 삽입되어 front에서 삭제된다.
2. rear: 데이터가 삽입되는 위치 (enqueue)
3. front: 데이터가 삭제되는 위치 (dequeue)

# 파이썬에서의 큐 연산자

1. append : enqueue 연산으로, rear에 데이터를 삽입한다.
2. popleft : dequeue 연산으로, front에 있는 데이터를 삭제한다.
   (rear와 반대 방향의 위치이므로 pop이 아닌 popleft)

# 공통점

-   스택과 큐 모두, 출력 시 먼저 삽입된 순서대로 출력된다.
-   나중에 삽입된 것부터 출력하고 싶다면, reverse() 메서드를 사용하여 순서를 뒤집어 출력하면 된다.
