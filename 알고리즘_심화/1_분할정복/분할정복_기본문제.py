def f(x,n):
    if n==1:
        return x
    else:
        result = 1
        for _ in range(1,1+n):
            result = result * x
        return result

print(f(2,4))