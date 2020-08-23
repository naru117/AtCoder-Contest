# 最小公倍数の求め方
import math
from functools import reduce


def lcm_base(p, q):
    return (p * q) // math.gcd(p, q)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


a_list = [3, 4, 20]
print(lcm_list(a_list))
# 60
