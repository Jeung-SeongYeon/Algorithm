def solution(n):
    divide_num = 1000000007
    unique_num = [12, 2, 4]

    dp = [1, 1, 3, 10]

    for i in range(4, n + 1):
        basic_num = dp[i - 1] + 2 * dp[i - 2] + 5 * dp[i - 3]
        
        if i > 6:
            unique_num[i % 3] += 2 * dp[i - 4] + 2 * dp[i - 5] + 4 * dp[i - 6]
            unique_num[i % 3] %= divide_num

        dp.append((basic_num + unique_num[i % 3]) % divide_num)

    return dp[n]
