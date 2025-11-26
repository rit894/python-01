books={
    'Aryavarta':{
        'author':'Vishnu Sharma',
        'price':500,
        'books count':3
    },
    'Harry potter':{
        'author':'J K Rowling',
        'price':3499,
        'books count':7
    },
    'Rich dad poor dad':{
        'author':'Robert T Kiyosaki',
        'price':799,
        'books count':1
    },
    'The alchemist':{
        'author':'J K Rowling',
        'price':299,
        'books count':1
    }
}
# 1st question
'''x=list(books)'''
# 2nd question
avg_num=[]
list1=[]
for count in books.values():
    if count['books count']:
        avg_num.append(count['books count'])
x=sum(avg_num)/len(books)
for name,count in books.items():
    if count['books count']>x:
        list1.append(name)
print(list1)
# 3rd question

author_dict = {}
for name, details in books.items():
    author = details['author']
    count = details['books count']    
    author_dict[author] = author_dict.get(author, 0) + count

print(author_dict)
# 4th question
p=[]
list2=[]
for price in books.values():
    if price['price']:
        p.append(price['price'])
x=sum(p)/len(p)
for name , details in books.items():
    if details['price']>x:
        list2.append(name)
print(list2)
# 5 question
A_dict={}
for name, details in books.items():
    authur=details['author']
    price = details['price']
    A_dict[authur]=A_dict.get(authur,0)+price
print(A_dict)





