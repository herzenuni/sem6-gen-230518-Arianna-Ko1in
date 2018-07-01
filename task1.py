def recursive_fibo(n):
    if n>=2:
        return recursive_fibo(n-1)+recursive_fibo(n-2)
    else:
        return 1

def fibo_list(n):
    return [ recursive_fibo(i) for i in range(0,n) ]

def fibo_yield(n):
    for i in range(0,n):
        yield recursive_fibo(i)

assert fibo_list(7)==[1,1,2,3,5,8,13]
assert list(fibo_yield(10))==[1,1,2,3,5,8,13,21,34,55]
