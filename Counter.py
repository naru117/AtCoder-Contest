import collections

A = [1, 2, 3, 4, 5]
B = [4, 5, 6, 7, 10]
a = collections.Counter(A)
b = collections.Counter(B)

print(a)
print(b)
# Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
# Counter({4: 1, 5: 1, 6: 1, 7: 1, 10: 1})

c = a | b
print(c)
# Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 10: 1})

d = a-b
print(d)
# Counter({1: 1, 2: 1, 3: 1})