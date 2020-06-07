"""
时间复杂度 和 空间复杂度 计算
"""
# 时间复杂度为O(1)
print('hello pg')
print('asdfqwer')

# O(n)
n = 100
for i in range(n):
    print(i)

# O(m * n)
m = 100
for i in range(n):
    for j in range(m):
        print('haha...')


# 空间复杂度为 1
a = 'python'
b = 'java'
c = 'C++'

# 5
num_list = [2, 43, 56, 32, 8]

# 3 * 2
num_list2 = [[1, 2], [3, 4], [5, 6]]


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