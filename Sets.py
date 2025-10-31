'''Sets
1.	Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.
Sample Input / Output:
Original sets:
{1, 2, 3, 4, 5, 6}
{3, 4, 5, 6, 7, 8}
Missing numbers in the second set as compared to the first:
{1, 2}
Missing numbers in the first set as compared to the second:
{8, 7}
set1 = {1, 2, 3, 4, 5, 6}
set2={3, 4, 5, 6, 7, 8}
M12=set2-set1
print(M12,'are missing in set1')
M21=set1-set2
print(M21, 'are missing in set 2')
2.	Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings.
 Sample Input: words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green'] 
 Sample Output: Unique Words: ['Red', 'Green', 'Blue'] and frequency of occurrence: {'Red': 4, 'Blue': 1, 'Green': 2}
forbd_char={'@','#','$'}
password=input("Enter a password : ")
print(set(password).intersection(forbd_char),'is forbidden to use .')
insta_followers={'a','b','c','d','e','f','g','h'}
twitter_followers={'c','d','x','y','z','v','w'}
print(twitter_followers.intersection(insta_followers),' are on both the  plateforms')
print(insta_followers-twitter_followers.intersection(insta_followers),'are exclusive to instagram')
print(insta_followers.union(twitter_followers)-twitter_followers.intersection(insta_followers),' are on atleast one account and dont overlap between the two ')
'''

