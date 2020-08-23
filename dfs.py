tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [], [], [], [], [], [], [], []]


def dfs(now):
    print(now)
    for i in tree[now]:
        dfs(i)


dfs(0)


# AtCoder Beginner Contest 151 D
# import numpy as np
# from collections import deque
# h, w = map(int, input().split())
# s = []
# for i in range(h):
#     s.append(list(input()))
#
#
# def bfs(i,j,dist):
#     seen[i][j] = dist
#     lis = [[i-1,j],[i,j-1],[i+1,j],[i,j+1]]
#     for place in lis:
#         if place[0]<0 or place[0]>=h or place[1]<0 or place[1]>=w:
#             continue
#         if seen[place[0]][place[1]] != -1 or s[place[0]][place[1]]=="#":
#             continue
#         if [place[0],place[1],dist+1] in que:
#             continue
#         que.append([place[0],place[1],dist+1])
#     if len(que):
#         new = que.popleft()
#         bfs(new[0],new[1],new[2])
#     else:
#         return
#
#
# mx = 0
# for i in range(h):
#     for j in range(w):
#         if s[i][j] == "#":
#             continue
#         seen = [[-1 for _ in range(w)]for _ in range(h)]
#         que = deque()
#         bfs(i, j, 0)
#         ast = np.array(seen)
#         tmp = np.amax(ast)
#         mx = max(mx, tmp)
#         #print(seen)
#         #print(*seen,sep="\n")
# print(mx)


# AtCoder Beginner Contest 151 D
# from collections import deque
# h, w = map(int, input().split())
# ma = [["#" for _ in range(w+2)] for _ in range(h+2)]
# for i in range(h):
#     tmp = list(input())
#     for j in range(w):
#         ma[i+1][j+1] = tmp[j]
# ans = 0
# for i in range(1, h+1):
#     for j in range(1, w+1):
#         if ma[i][j] == "#":
#             continue
#         elif ma[i][j] == ".":
#             p = [[-1 for _ in range(w+2)] for _ in range(h+2)]
#             p[i][j] = 0
#             q = deque()
#             q.append([i, j])
#             while q:
#                 y, x = q.popleft()
#                 if ma[y+1][x] == "." and p[y+1][x] == -1:
#                     p[y+1][x] = p[y][x] + 1
#                     q.append([y+1, x])
#                 if ma[y-1][x] == "." and p[y-1][x] == -1:
#                     p[y-1][x] = p[y][x] + 1
#                     q.append([y-1, x])
#                 if ma[y][x+1] == "." and p[y][x+1] == -1:
#                     p[y][x+1] = p[y][x] + 1
#                     q.append([y, x+1])
#                 if ma[y][x-1] == "." and p[y][x-1] == -1:
#                     p[y][x-1] = p[y][x] + 1
#                     q.append([y, x-1])
#             for l in range(1, h+1):
#                 ans = max(ans, max(p[l]))
#             # ans = max(ans, max(max(p)))
# print(ans)

