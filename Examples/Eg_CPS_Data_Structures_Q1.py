''' In computer networking, a ”packet” is a unit of data sent over a network. When debugging network
 issues, it’s common to analyze a stream of packets to look for anomalies. One common anomaly is a
 duplicate packet, which can be identified by its unique sequence number (an integer).
 You are tasked with building a program for a network monitoring tool. Write a Python function
 called find
 duplicate
 packets that takes a list of packet sequence numbers (integers).
 This function should process the list and return a dictionary where:
 • The keys are the sequence numbers that appeared more than once.
 • The values are the total counts of how many times that duplicate sequence number appeared.
 If no duplicates are found, the function should return an empty dictionary'''
def find_duplicate_packets(list_numbers):
    dict_numbers={}
    for char in list_numbers:
        if list_numbers.count(char)>1:
            dict_numbers[char] = list_numbers.count(char)
    print(dict_numbers)
        
find_duplicate_packets(list_numbers=[1,2,3,4,5,1,2,3,1,2,1])
list_numbers=[]
n=int(input("Enter the number of packets: "))
for i in range(n):
    num=int(input("Enter the packet sequence number: "))
    list_numbers.append(num)
find_duplicate_packets(list_numbers)
# Aditya code
'''nums = {}
numbers = input("ENTER NUMBERS : ").split()
def dict_nums(nums) :
    for i in numbers :
        count = numbers.count(i)
        if count == 1 :
            continue
        elif  count > 1 :
            nums[i] = count
dict_nums(nums)
print(nums)'''