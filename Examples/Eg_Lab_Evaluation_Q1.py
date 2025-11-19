name_list=["Alice", "Bob", "Charlie", "David", "Eva"]
basic_info=[('Alice',2020), ('Bob',2019), ('Charlie',2021), ('David',2018), ('Eva',2022)]
activities_set={'Hiking', 'Swimming', 'Reading', 'Traveling', 'Cooking'}
membership_status_dict={'Alice':'Active',
                        'Bob':'Inactive',
                        'Charlie':'Active',
                        'David':'Active',
                        'Eva':'Inactive'}
# Question A
def add_student(name_list,basic_info,membership_status_dict):

    new_name1=input().split(',')
    name_list.extend(new_name1)
    print(f' student {new_name1} added succesfully ')

    for name in new_name1:
        tuple_new=(name,int(input()))
        basic_info.append(tuple_new)

    for name in new_name1:
        membership_status_dict[name]='Active'
    print(name_list)
    print(basic_info)
    print(membership_status_dict)

# Question B
def updated_activities(activities_set,new_activity):

    

        if new_activity in activities_set:
            print(f'{new_activity} is already in the activities list ')
        elif new_activity not in activities_set:
            activities_set.add(new_activity)
            print(f'Activity {new_activity} added ')
        print(activities_set)

# Question C
def check_membership(status_dict, check_name):
    tuple1=[]
    

    if check_name in membership_status_dict:
          tuple1.append(membership_status_dict.get(check_name))
          

    count=0
    for names in membership_status_dict.values():
        if names=='Active':
            count+=1
        tuple1.append(count)
    print(tuple(tuple1))

# Question D
N=int(input())
for i in range(N):
    choosing=int(input())
    if choosing==1:
        add_student(name_list,basic_info,membership_status_dict)
    elif choosing==2:
        new_activity=input()
        updated_activities(activities_set,new_activity)
        
    elif choosing==3:
         status_dict=membership_status_dict
         check_name=input()
         check_membership(status_dict, check_name)
        


        
        
         
      



