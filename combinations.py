import itertools
# 1~cの中からk個選ぶときの選び方
c = 5
k = 2
c_list = [i+1 for i in range(c)]
for C in itertools.combinations(c_list, k):
    print(C)
# (1, 2)
# (1, 3)
# (1, 4)
# (1, 5)
# (2, 3)
# (2, 4)
# (2, 5)
# (3, 4)
# (3, 5)
# (4, 5)

# 1~pの順列
p = 3
p_list = [i for i in range(1, p+1)]
for P in itertools.permutations(p_list):
    print(P)
# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (2, 3, 1)
# (3, 1, 2)
# (3, 2, 1)
