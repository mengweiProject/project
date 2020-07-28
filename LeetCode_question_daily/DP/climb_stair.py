"""
爬楼梯

动态规划
总结动态方程
设定初始值
"""

from Helper.Tools import calc_run_time


# @calc_run_time
def calc_climb_stair(n):
    fst = 1
    scd = 2
    ret = 0
    for i in range(2, n):
        ret = fst + scd
        fst = scd
        scd = ret
    return max(n, ret)


def calc_climb_stair2(n):
    fst = 1
    scd = 2
    result = 0
    for i in range(2, n):
        result = fst + scd
        fst = scd
        scd = result
    return max(n, result)


if __name__ == '__main__':
    n = 1
    print(calc_climb_stair(n))
    print(calc_climb_stair2(n))