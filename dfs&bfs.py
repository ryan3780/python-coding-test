from collections import deque

# stack
# 선입 후출 구조 또는 후입 선출 구조

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

#최하단 원소부터 출력
print('stack: ', stack)

#최상단 원소부터 출력
print('stack: ', stack[::-1])
# que
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
# 재귀 함수

# 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 ㅘ정

# 자료구조란 데이터를 표현하고 관리하고 처리하기 위한 구조

# 오버플로와 언더플로

