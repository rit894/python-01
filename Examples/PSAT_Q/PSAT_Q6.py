'''Given an array  arr  of integers. Find a peak element  i.e. an element that is  not  smaller  than its neighbors. 
 Note:  For corner elements, we need to consider only  one neighbor. 
 Example: 
 Input:  array[]= {5, 10, 20, 15} 
 Output:  20 
 Explanation:  The element 20 has neighbors 10 and 15,  both of them are less  than 20. 
 Input:  array[] = {10, 20, 15, 2, 23, 90, 67} 
 Output:  20   90'''
n=[1,2,3,5,4]
list1=[]
if n[0]>n[1]:
        list1.append(n[0])
if n[len(n)-1]>n[len(n)-2]:
        list1.append(n[len(n)-1])
for i in range(len(n)):
    if n[i]==n[0] or n[i]==n[len(n)-1]:
           continue
    elif  n[i-1]<n[i]>n[i+1]:
           list1.append(n[i])
print(list1)
# Q2
n=[1,2,3,5,4,-5,-8,9,-2]
list1=[]
list2=[]
for i in range(len(n)):
     if n[i]<0:
            list1.append(n[i])
     else:
            list2.append(n[i])
print(list1)
print(list2)
list1.extend(list2)
print(list1)      

# Question 3
x=[1,2,3,4,5,6]
sum=int(input())
list1=[]
if x[0]+x[1]== sum:
       tuple1=(x[0],x[1])
       list1.append(tuple1)
if x[len(x)-1]+x[len(x)-2]== sum:
       tuple1=(x[len(x)-1],x[len(x)-2])
       list1.append(tuple1)
for i in range(len(x)):
    for j in range(len(x)):
           if x[i]+x[j]==sum:
              tuple1=(x[i],x[j])
              list1.append(tuple1)
print(list1 ,len(list1) )

    
                


