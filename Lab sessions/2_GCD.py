def GCD(n,m):
    if n % m ==0:
        return m
    else:
        x= n % m
        return GCD(m,x)
print(GCD(20,16))