'''International Language Society keeps track of the following details related to each country – Name 
of the country, Total land area, and the number of languages used (including official and unofficial 
languages used in the country). The organization has approached you to do some analysis on their 
data. Unluckily, they do not have the soft copy of their data. You need to enter the details for N 
countries and find answers for the following two questions:  
 Which country has the maximum number of languages?  
 Which country has the highest Area/Language count ratio?  
Design and implement a nested list-based Python solution to read the details of N countries and 
answer the above questions. [10 marks] [CO2] [BTL3]  
Input Format  
The first input is the number of countries, N. The next 3*N inputs are the Name of the country (a 
string), Area (a number), and Languages (another integer) for each country.  
Output Format  
The program prints the country's name with a maximum number of languages and the 
corresponding language count in the first line. The second line prints the country's name with the 
highest (Area / Languages) ratio. If multiple countries satisfy the above criteria, print the first 
country's details alone. Sample inputs and corresponding expected outputs along with explanations 
are provided for better understanding. '''
N=int(input())
countries={}
for i in range(N):
    country_name= input()
    area_of_country=float(input())
    language_count=int(input())
    countries[country_name]={
        'area': area_of_country,
        'languages': language_count
    }
def max_lan_count():
    dict1={}
    for country,language in countries.items():
            dict1[country]=language['languages']
    for country, count in dict1:
         if count== max(dict1.values()):
              print(country,count)
def max_arealan_ratio():
    dict1={}
    for country,language in countries.items():
            dict1[country]=language['area']/language['languages']
    for country, count in dict1.items():
         if count== max(dict1.values()):
              print(country)
max_arealan_ratio()
max_lan_count()