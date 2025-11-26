product_ID=(101,102,103,104,105)
previous_week_sales=(2500,3000,4000,1500,2000)
currenrt_week_sales=(2700,2900,4100,1600,2100)
print(product_ID)
print(previous_week_sales)
print(currenrt_week_sales)
list1=[]
higher=[]
lower=[]
equal=[]
for i , j,k in zip(list(previous_week_sales),list(currenrt_week_sales),list(product_ID)):
    x=i-j
    list1.append(x)
    if j>i:
        higher.append(k)
    elif j<i:
        lower.append(k)
    else:
        equal.append(k)

# Question 2
print(list1)
# Question 3
print(len(higher))
print(len(lower))
print(len(equal))
# Question 4
if len(higher)>len(lower) and len(higher)>len(equal):
    print('profit')
elif len(lower)>len(higher) and len(lower)>len(equal):
    print('loss')
else:
    print('neither loss nor gain')
