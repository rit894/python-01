objects = {
    'Dune': {
        'IMDB_rating': 8.5,
        'Duration': 166,
        'category': 'PG-13'
    },
    'Deadpool': {
        'IMDB_rating': 7.8,
        'Duration': 128,
        'category': 'R'
    },
    'Furiosa': {
        'IMDB_rating': 7.5,
        'Duration': 148,
        'category': 'R'
    },
    'Longlegs': {
        'IMDB_rating': 6.2,
        'Duration': 95,
        'category': 'PG'
    },
    'Civil War': {
        'IMDB_rating': 7.8,
        'Duration': 147,
        'category': 'PG-13'
    },
    'Abigail': {
        'IMDB_rating': 5.1,
        'Duration': 99,
        'category': 'R'
    }
}
# 1st question

'''x=list(objects)'''
# 2nd question

list1=[]
for name,duration in objects.items():
    if duration['Duration']>145:
        list1.append(name)
print(list1)

# 3rd question
rating=[]
list2=[]
for ratings in objects.values():
    if ratings['IMDB_rating']:
        rating.append(ratings['IMDB_rating'])
x=sum(rating)/len(rating)
for name,ratings in objects.items():
    if ratings['IMDB_rating']>x:
        list2.append(name)
print(list2)

# 4th question
r=[]
pg=[]
for category in objects.values():
    if category['category']=='R':
        r.append(category['Duration'])
        
    elif category['category']=='PG-13':
        pg.append(category['Duration'])
print("R:",sum(r)/len(r))
print("PG-13:",sum(pg)/len(pg))

# 5th question
r=[]
pg=[]
for category in objects.values():
    if category['category']=='R':
        r.append(category['IMDB_rating'])
        
    elif category['category']=='PG-13':
        pg.append(category['IMDB_rating'])
print("R:",sum(r)/len(r))
print("PG-13:",sum(pg)/len(pg))



    
 
