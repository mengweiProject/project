"""
每日一题
始于：2020-05-22
终于：希望不会有这一天
"""

from time import time
from datetime import datetime

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


def q4(*parm):
    # 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
    #  请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 你可以假设 nums1 和 nums2 不会同时为空。
    #  示例 1:
    #  nums1 = [1, 3]
    #  nums2 = [2]
    #  则中位数是 2.0
    # 示例 2:
    #  nums1 = [1, 2]
    #  nums2 = [3, 4]
    #  则中位数是(2 + 3) / 2 = 2.5
    if len(parm[0]) == 0 and len(parm[1]) == 0:
        print('None')
        return
    else:
        # print(parm[0] + parm[1])
        l = parm[0] + parm[1]
        l.sort()
        print(l)
        if len(l) % 2 != 0:
            print(len(l) // 2)
            median = l[len(l) // 2]
        else:
            print(l[(len(l) - 1) // 2], l[(len(l) + 1) // 2])
            median = (l[(len(l) - 1) // 2] + l[(len(l) + 1) // 2]) / 2
        print(median)


def q4_2():
    m = 10
    n = 11
    print(int((m + n) / 2))
    # 编程语言中，取整，一般都是向下取整。如：10.5，取整为10，-10.5，取整为-11


def q4_3(num1, num2):
    if len(num1) > len(num2):
        num1, num2 = num2, num1
    # print(len(num1) % 2)
    if len(num1) % 2 == 1:
        m = int(len(num1) / 2 + 1)
    else:
        m = int(len(num1) / 2)
    n = int((len(num1) + len(num2) + 1) / 2 - m)

    while True:
        a = max(num1[m - 1], num2[n - 1])
        b = min(num1[m], num2[n])
        if a > b:
            m += 1
            n -= 1
        if a < b:
            break
    if (len(num1) + len(num2)) % 2 == 0:
        print(a, b)
        return (a + b) / 2
    return a


# 回文字符串
def q5(s):
    # 给定一个字符串
    # s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
    #  示例 1：
    # 输入: "babad"
    # 输出: "bab"
    # 注意: "aba"
    # 也是一个有效答案。
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    res = ""
    for i in range(n):
        for j in range(i + 1):
            if s[i] == s[j] and (i - j + 1 <= 3 or dp[j + 1][i - 1]):
                dp[j][i] = 1
                res = max(res, s[j: i + 1], key=len)
    return res


def q5_1(s):
    size = len(s)
    if size < 2:
        return s
    dp = [[False for _ in range(size)] for _ in range(size)]
    # for v in dp:
    #     print(v)
    max_len = 1
    start = 0

    for i in range(size):
        dp[i][i] = True
    # for v in dp:
    #     print(v)
    for j in range(1, size):
        for i in range(0, j):
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False

            if dp[i][j]:
                cur_len = j - i + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start = i
    print(s[start: start + max_len])
    return s[start: start + max_len]


def q5_2(s):
    size = len(s)
    if size < 2:
        return s
    dp = [[False for _ in range(size)] for _ in range(size)]
    max_len = 1
    start = 0
    for i in range(size):
        dp[i][i] = True

    for j in range(1, size):
        for i in range(0, j):
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False

            if dp[i][j]:
                cur_len = j - i + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start = i
    return s[start: start + max_len]


def q5_3(s):
    size = len(s)
    if size < 2:
        return s
    dp = [[False for _ in range(size)] for _ in range(size)]
    max_len = 1
    start = 0
    for i in range(size):
        dp[i][i] = True
    for j in range(1, size):
        for i in range(0, j):
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False

            if dp[i][j]:
                cur_len = j - i + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start = i
    return s[start: start + max_len]


class Q84():
    def q84(self, heights):
        # 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
        #  求在该柱状图中，能够勾勒出来的矩形的最大面积。
        # 思路：中心扩散
        max_area = 0
        for idx in range(len(heights)):
            if heights[idx] == 0:
                area = 0
            else:
                area = self.calc_area(idx, heights)
            if max_area < area:
                max_area = area
        return max_area


    def calc_area(self, idx, heights):
        left_idx = idx
        right_idx = idx
        if len(heights) == 1:
            return heights[idx]
        if idx == 0:
            while True:
                right_idx += 1
                if right_idx == len(heights):
                    right_idx -= 1
                    break
                if heights[0] > heights[right_idx]:
                    right_idx -= 1
                    break

        elif idx == len(heights) - 1:
            right_idx = idx
            left_idx = idx
            while True:
                left_idx -= 1
                if left_idx < 0:
                    left_idx += 1
                    break
                if heights[idx] > heights[left_idx]:
                    left_idx += 1
                    break
        else:
            while True:
                left_idx -= 1
                if heights[left_idx] < heights[idx]:
                    left_idx += 1
                    break
                if left_idx == 0:
                    break

            while True:
                right_idx += 1
                if heights[right_idx] < heights[idx]:
                    right_idx -= 1
                    break
                if right_idx == len(heights) - 1:
                    break
        return heights[idx] * (right_idx - left_idx + 1)


def longest_sub_str(s):
    """
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    示例 1:

    输入: "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    """
    if len(s) == 0:
        return None
    elif len(s) == 1:
        return 1
    else:
        start_idx = 0
        max_len = 1
        hash_dict = {}
        for i, v in enumerate(s):
            if v in hash_dict and hash_dict[v] > start_idx:
                start_idx = hash_dict[v]
                hash_dict[v] = i
            else:
                hash_dict[v] = i
                max_len = max(max_len, i - start_idx)
        return max_len



if __name__ == '__main__':
    s = "abca"
    print(longest_sub_str(s))