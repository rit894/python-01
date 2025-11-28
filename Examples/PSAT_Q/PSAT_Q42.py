N=int(input())
A=list(map(int,input().split()))
a=[]
for num in A:
   a.append(str(num%10))
a=''.join(a)
if int(a)%10==0:
   print('yes')
else:
   print('No')