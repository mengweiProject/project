"""
每日一题
始于：2020-05-22
终于：希望不会有这一天
"""

from datetime import datetime
from time import time

def run_time(func):
    def inner_func(*parm):
        begin_time = datetime.now()
        ret = func(*parm)
        end_time = datetime.now()
        print(end_time - begin_time)
        return ret
    return inner_func

@run_time
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


@run_time
def q2(*parm):
    """
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
    """
    carry = 0
    if len(parm[0]) > len(parm[1]):
        parm[1].extend([0 for i in range(len(parm[0]) - len(parm[1]))])
    else:
        parm[0].extend([0 for i in range(len(parm[1]) - len(parm[0]))])
    print(parm[0])
    print(parm[1])

    for idx in range(len(parm[0])):
        number = parm[0][idx] + parm[1][idx] + carry
        if number >= 10:
            parm[0][idx] = 0 + carry
            carry = 1
        else:
            parm[0][idx] = number
            carry = 0
        if number >= 10 and idx == len(parm[0]) - 1:
            parm[0].extend([1])
    print(parm[0])

def q3(*parm):
    # 给定一个字符串，请你找出其中不含有重复字符的
    # 最长子串
    # 的长度。
    # 输入: "abcabcbb"
    # 输出: 3
    # 解释: 因为无重复字符的最长子串是
    # "abc"，所以其长度为 3。
    start_idx = 0
    end_idx = 1
    max_len = end_idx - start_idx
    if len(parm[0]) == 1:
        print(max_len)
        return
    while end_idx < len(parm[0]):
        if parm[0][end_idx] in parm[0][start_idx: end_idx]:
            start_idx += 1
        else:
            end_idx += 1
        lens = len(parm[0][start_idx: end_idx])
        if lens > max_len:
            max_len = lens
        # print(parm[0][start_idx: end_idx])
    print(max_len)


def q3_2(*parm):
    max_len = 0
    start_idx = 0
    end_idx = 1
    if len(parm[0]) > 1:
        while end_idx <= len(parm[0]):
            sub_set = set(parm[0][start_idx: end_idx])
            sub_lst = parm[0][start_idx: end_idx]
            # print(sub_set, sub_lst)
            if len(sub_set) == len(sub_lst):
                end_idx += 1
            else:
                start_idx += 1
            if len(sub_lst) > max_len and len(sub_set) == len(sub_lst):
                max_len = len(sub_lst)
                # print(max_len)
    print(max_len)




if __name__ == '__main__':
    q3('pwwkew')
    q3_2('pwwkew')

