'''flowers={'hibiscus':{
     'unit price':100,
     ' no of colours available':6,
     'colours avialable':'Red,white,pink,violet,orange,yellow'},

     'rose':{
     'unit price':200,
     ' no of colours available':4,
     'colours avialable':'Red,white,maroon,yellow'},

     'marigold':{
     'unit price':50,
     ' no of colours available':2,
     'colours avialable':'orange,yellow'},

     'dahlia':{
     'unit price':150,
     ' no of colours available':3,
     'colours avialable':'Red,white,pink'},

     'lotus':{
     'unit price':300,
     ' no of colours available':3,
     'colours avialable':'blue, pink,yelow'}


}
q1='which flower has maximun clour variation?'
q2='choosing colour and getting to know its clour shades '
q3='billing of the flowers '
q4='unique colours'
menu=input(f'chosse among the following questions \nif yes please enter coresspondingly\n{q1}(y)\n{q2}(y1)\n{q3} (y2)\n{q4}(y3)')
print(menu)
if menu=='y':
   if flowers['hibiscus'][' no of colours available']>flowers['rose'][' no of colours available'] and flowers['hibiscus'][' no of colours available']>flowers['marigold'][' no of colours available'] and flowers['hibiscus'][' no of colours available']>flowers['dahlia'][' no of colours available'] and flowers['hibiscus'][' no of colours available']>flowers['lotus'][' no of colours available']:
       print('hibiscus has maximum colour variation')           '''
'You are given two sorted arrays of integers representing two branches’ sales data. Write'
'''def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    total_length = len(arr1) + len(arr2)

    for _ in range(total_length):
     
        if i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
      
        elif i < len(arr1):
            merged.append(arr1[i])
            i += 1
       
        else:
            merged.append(arr2[j])
            j += 1

    return merged

def read_sorted_list(prompt):
    s = input(prompt).strip()
    if not s:
        return []
    return list(map(int, s.split()))

arr1 = read_sorted_list("Enter sorted integers for arr1 separated by spaces (or leave empty): ")
arr2 = read_sorted_list("Enter sorted integers for arr2 separated by spaces (or leave empty): ")
merged = merge_sorted_arrays(arr1, arr2)
print("Merged:", merged)'''
import array

# Input first sorted array
arr1 = array.array('i', [])
n1 = int(input("Enter size of first sorted array: "))
for i in range(n1):
    val = int(input(f"Enter element {i+1}: "))
    arr1.append(val)

# Input second sorted array
arr2 = array.array('i', [])
n2 = int(input("\nEnter size of second sorted array: "))
for i in range(n2):
    val = int(input(f"Enter element {i+1}: "))
    arr2.append(val)

# Combine both arrays
merged = array.array('i', [])
for i in arr1:
    merged.append(i)
for j in arr2:
    merged.append(j)

# Now sort the merged array manually using for loops (Bubble sort)
for i in range(len(merged)):
    for j in range(i + 1, len(merged)):
        if merged[i] > merged[j]:
            merged[i], merged[j] = merged[j], merged[i]

a=set(merged)
print("\nMerged sorted array:", list(a))
