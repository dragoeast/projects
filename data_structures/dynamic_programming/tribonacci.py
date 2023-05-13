def tribonacci(n):
    return _tribonacci(n, memo={})

def _tribonacci(n, memo):
    key = n
    if key in memo:
        return memo[key]
    
    if n in [0, 1]:
        return 0
    if n == 2:
        return 1
    
    memo[key] = sum( [ _tribonacci(n-i, memo) for i in range(1, 3+1) ] )
    return memo[key]

for _ in range(100):
    print(f"{_}--->{tribonacci(_)}")
