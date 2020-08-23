import numpy as np
n = int(input())
a = [int(x) for x in input().split()]

m = np.zeros(max(a)+1, dtype=int)
cnt = 0

for i in a:
    m[::i] += 1
for i in a:
    if m[i] == 1:
        cnt += 1
print(cnt)
