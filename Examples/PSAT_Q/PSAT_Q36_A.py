dict_1={}
def calculate_salary():
    n=int(input())
    for i in range(n):
            i_d=input()
            HRA=float(input())
            Basic_pay=int(input())
            dict_1[i_d]=dict_1.get(i_d,0)+HRA+Basic_pay
    sorted_salary=sorted(dict_1.values())
    print("Sorted salary list is:",sorted_salary)
    return dict_1

def Highest_salary(dict_1):
    x=max(dict_1.values())
    for id,salary in dict_1.items():
        if salary==x:
            return id
sorted_salary=sorted(dict_1.values())

print(calculate_salary())
print("ID with highest salary is:",Highest_salary(dict_1))
dict_1 = {}

'''
def calculate_salary():
    n = int(input("Enter number of employees: "))
    for i in range(n):
        i_d = input("Enter employee ID: ")
        HRA = float(input("Enter HRA: "))
        Basic_pay = int(input("Enter Basic Pay: "))
        dict_1[i_d] = dict_1.get(i_d, 0) + HRA + Basic_pay
    
    # Compute sorted salary list after filling dictionary
    sorted_salary = sorted(dict_1.values())
    print("Sorted salary list is:", sorted_salary)
    return dict_1

def Highest_salary(dict_1):
    max_salary = max(dict_1.values())
    # Collect all IDs with the maximum salary
    highest_ids = [id for id, salary in dict_1.items() if salary == max_salary]
    return highest_ids, max_salary

# Run
salary_dict = calculate_salary()
highest_ids, max_salary = Highest_salary(dict_1)
print("Salary dictionary:", salary_dict)
print("ID(s) with highest salary:", highest_ids, "with salary:", max_salary)'''




