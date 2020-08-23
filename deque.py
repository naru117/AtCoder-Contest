from collections import deque

S = 'abcdefg'
s = deque(S)

print(s.appendleft('l'))
# deque(['l', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])

print(s.append('r'))
# deque(['l', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'r'])

print(s.reverse())
# deque(['r', 'g', 'f', 'e', 'd', 'c', 'b', 'a', 'l'])

print(s.pop())
# l

print(s.popleft())
# r
