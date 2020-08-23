n, k = map(int, input().split())
a = list(map(int, input().split()))

d = [0] * n
d[0] = 1
t = a[0]
cnt = 0
r = [1]

while d[t-1] == 0:
    cnt += 1
    d[t-1] = cnt + 1
    if k == cnt:
        print(t)
        exit()
    r.append(t)
    t = a[t-1]

rp = r[d[t-1]-1:]
b = (k-cnt) % len(rp)
print(rp[b-1])