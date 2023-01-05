def prem(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 

for n in range(2, 1001):
    if prem(n):
        print(n)                