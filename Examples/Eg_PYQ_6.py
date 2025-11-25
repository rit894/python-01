'''Read the register number (3-digit integer values) and GPA (a real number between 0.0 and 
10.0) for N students. Number of students (N) is accepted as an input from the user. Construct 
a Dictionary using register number as Key and GPA as the value. The summer internship 
eligibility criterion for a student is a GPA of more than 7. Write a menu-driven python 
program that does the following based on the option selected. [15 marks] [CO2] [BTL3]  
1. Print the contents of the dictionary.  
2. Display the count of students eligible for summer internships.  
3. Print the average GPA of students who are not eligible for internship.  
4. Out of all students who are not eligible for internship, display the student register number 
who has the least difference between current GPA and eligibility cut-off value 7.  
5. Out of the Internship-eligible students, display the student register number who scored the 
highest GPA. '''
students_GPA = {}
N=int(input())
for i in range(N):
    regi_number=int(input())
    GPA=int(input())
    students_GPA[regi_number]=GPA
print(students_GPA)
count_internships=[]
not_eligible=[]
least=0
reg=0
for key,value in students_GPA.items():
    if value>7:
       count_internships.append(key)
    elif value<=7:
       not_eligible.append(value)
    if 7-value>least:
        least=7-value
        reg=key
print(len(count_internships))
count=0
if sum(not_eligible)==0 or len(not_eligible)==0:
    print(0)
else:
 print(sum(not_eligible)/len(not_eligible))


print(reg)
print(students_GPA.get(max(count_internships)))


