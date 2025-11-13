'''points2D=[(1,2),(5,6),(3,4),(7,-8)]

points2D_sorted=sorted(points2D, key=lambda x: x[1])

print(points2D_sorted)
print(points2D)
'''
#ambda function to convert a string to its upper case using upper()
'''s1 = 'GeeksforGeeks'
s2 = lambda func: func.upper()
print(s2(s1))'''
# lambda function uses nested if-else logic to classify numbers as Positive, Negative or Zero.
'''n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))   
print(n(-3))  
print(n(0))'''
#Using with List Comprehension
'''li=[lambda arg=x: arg*10 for x in range(1,6)]
for item in li:
    print(item())'''
#Using for Returning Multiple Results
'''x=lambda a,b: (a+b, a-b, a*b, a/b)
result=x(10,5)
print(result)'''
