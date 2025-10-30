'''
def greet(n):
    return f"Hello, {n}!"

n= input("Enter your name: ")
print(greet(n))
def addNum(a,b):
    return a + b
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
print("The sum is:", addNum(a,b))
def iseven(n):
    if n%2==0:
        return True
    else:
        return False
num= int(input("Enter a number: "))
print(iseven(num))
def square(n):
    return pow(n,2)
n=int(input("Enter a number to find its square: "))
print("The square of", n, "is", square(n))''
def revstr(s):
    return s[::-1]  
s= input("Enter a string to reverse: ")
print("The reversed string is:", revstr(s))
def factorial(n):
    result=1
    for i in range(1,n+1):
     result = result * i
    return result
n=int(input('number : '))
print(f'factorial of {n} is {factorial(n)}')'''
def palindrome_check(s):
    if s==s[::-1]:
        return "is"
    else:
        return "is not"
    
s=input ( 'text plz: ')
print(f'the word{s} {palindrome_check(s)}  palinlindrome')



