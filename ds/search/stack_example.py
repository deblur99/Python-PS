# 스택은 LIFO (Last In First Out)
# -> 스택은 마지막에 삽입된 요소를 top으로 관리한다. top으로 삽입되고 top으로 삭제된다.

# 파이썬에서의 스택 연산자 -> 파이썬에서는 -1번 인덱스가 top으로 간주된다.
# 1. append : top에 데이터를 삽입한다.
# 2. pop : top에 있는 데이터를 삭제한다.

stack = list()

# stack은 LIFO (Last In First Out)
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

stack.append(50)
print(stack)

stack.pop()
print(stack)