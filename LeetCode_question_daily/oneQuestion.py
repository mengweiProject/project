"""
每日一题
始于：2020-05-22
终于：希望不会有这一天
"""

from datetime import datetime
from time import time

def program_run_time(func):
    def inner_func(*parm):
        begin_time = datetime.now()
        ret = func(*parm)
        end_time = datetime.now()
        print(end_time - begin_time)
        return ret
    return inner_func

@program_run_time
def q1(*parm):
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
    示例:
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
    :return:
    """
    n = parm[0]
    for i in parm[0]:
        for j in parm[0]:
            if i + j == parm[1]:
                return n.index(i), n.index(j)


def q1_2(*parm):
    hashmap = {}
    for idx, element in enumerate(parm[0]):
        hashmap[element] = idx
    # print(hashmap)
    for idx, element in enumerate(parm[0]):
        a = hashmap.get(parm[1] - element)
        if a is not None and idx != a:
            print(idx, a)
            return 



if __name__ == '__main__':
    q1_2([1, 2, 3, 4, 5], 9)