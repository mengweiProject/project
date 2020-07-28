"""
买卖股票的最佳时机

动态规划
"""


def calc_best_time(arr):
    # print(arr)
    result_list = []
    for i in range(len(arr)):
        for j in range(i):
            result_list.append(arr[i] - arr[j])
    return max(result_list)


def calc_best_time2(arr):
    """
    记录：到当前日期的最小净值
    记录：到当前日期的最大收益
    """
    smst_nav = float('inf')
    # print(smst_nav)
    largest_pro = 0
    for nav in arr:
        smst_nav = min(smst_nav, nav)
        # print(smst_nav)
        largest_pro = max(largest_pro, nav - smst_nav)
    return largest_pro


def calc_stock_time3(nav_list):
    n = len(nav_list)
    dp = [0] * n
    print(dp)
    min_v = nav_list[0]
    for idx, v in enumerate(nav_list):
        min_v = min(min_v, v)
        dp[idx] = max(dp[idx], v - min_v)

    return max(dp)



if __name__ == '__main__':
    arr = [7, 1, 4, 5, 6, 3]
    print(calc_best_time(arr))
    print(calc_best_time2(arr))
    print(calc_stock_time3(arr))