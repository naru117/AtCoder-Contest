tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [], [], [], [], [], [], [], []]

from collections import deque

queue = deque([0])
while queue:
    now = queue.popleft()
    print(now)
    for i in tree[now]:
        queue.append(i)

# AtCoder Beginner Contest 168 D
# from collections import deque
# n, m = map(int, input().split())
# g = [[] for _ in range(n)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     g[a-1].append(b-1)
#     g[b-1].append(a-1)
# print(g)
# q = deque([0])
# d = [-1]*n
# d[0] = 0
# ans = [0]*n
# print('Yes')
# while q:
#     p = q.popleft()
#     for node in g[p]:
#         if d[node] == -1:
#             d[node] = d[p] + 1
#             q.append(node)
#         else:
#             if d[node] + 1 == d[p]:
#                 ans[p] = node + 1
# for i in range(1, n):
#     print(ans[i])
# print(d)