diff = 0.00001
def is_ok(n,ans):
    return abs(ans**2-n) < diff
def get_better(n,ans):
    return ((float(n)/ans + ans))/2
def my_sqr(n):
    ans = 1
    while not is_ok(n,ans):
        ans = get_better(n,ans)
    return ans

        
