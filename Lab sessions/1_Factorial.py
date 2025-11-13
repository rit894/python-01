
def factorial(n):
    print(f'the factorial function of {n} is called')
    if n==0:
       return 1
    else:
         x=n*factorial(n-1)
         print(x,'is the factorial of ',n)
         return x
print(factorial(5))
      