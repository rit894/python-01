numlist=[3,4,5,2,1]
'''n=0
list1=[]
for i in numlist:
    if i>=n:
        list1.append(i)
        i=n
print(list1)'''
numlist=[3,4,5,2,1]
numlist_copy=numlist.copy()
list1=[]
for i in range(len(numlist)):
    for char in numlist_copy:
        if char==min(numlist_copy):
            numlist_copy.remove(char)
            list1.append(char)
print(list1)
print(numlist)
numlist = [3, 4, 5, 2, 1]

# Bubble Sort
for i in range(len(numlist)):                  # Outer loop → number of passes
    for j in range(1, len(numlist) - i):       # Inner loop → shrinking range
        if numlist[j] < numlist[j-1]:          # Compare consecutive elements
            # Swap if out of order
            numlist[j], numlist[j-1] = numlist[j-1], numlist[j]

print("Sorted list:", numlist)
numlist = [3, 4, 5, 2, 1]

# Selection Sort
for i in range(len(numlist)):                 # Outer loop → position to fill
    smallest_index = i                        # Assume current index is smallest
    for j in range(i+1, len(numlist)):        # Inner loop → search in remaining list
        if numlist[j] < numlist[smallest_index]:
            smallest_index = j                # Update smallest index
    
    # Swap the found smallest with the element at position i
    numlist[i], numlist[smallest_index] = numlist[smallest_index], numlist[i]

print("Sorted list:", numlist)
