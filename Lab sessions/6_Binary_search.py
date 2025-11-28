x=[10, 15, 20, 23, 30, 35, 40]
target_element=20
found=False
low=0
high=len(x)
while found==False:
 mid_index=(low+high)//2
 if target_element<x[mid_index]:
    high=mid_index
    if target_element==x[mid_index]:
     found==True
 else:
   low=mid_index
   if target_element==x[mid_index]:
    found==True
