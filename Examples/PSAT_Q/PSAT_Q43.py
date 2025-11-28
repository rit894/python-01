# Another methode for doing this Question 
N=int(input())
K=int(input())
list1=list(map(int,input().split()))
list2=[]
for j in range(K):
 for i in range(len(list1)-1):
    if list1[i]==min(list1):
      list2.append(list1[i])
      list1.remove(list1[i])
print(list2)