DIV = 1000000000

def fibo(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append((dp[i-1] + dp[i-2]) % DIV)
    return dp[n]

n = int(input())
result = fibo(abs(n))
if n < 0:
    print(int((-1) ** (n+1)))
    print(result)
elif n > 0:
    print(1)
    print(result)
else:
    print(0)
    print(0)