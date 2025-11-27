word=input().lower()
z=0
o=0
for i in range(len(word)):
    if word[i]=='z':
        z+=1
    elif word[i]=='o':
        o+=1
if 2*z==o:
    print('yes')
else:
    print('no')
# SET 2
n=input('DDXDDD-DD')
validity_list=[1,1,1,1,1]
validity_check=[]
if n[2] in "AEIOU":
  validity_check.append(1)
for i in range(len(n)):
    if n[i].isdigit() and n[i+1].isdigit():
        if n[i]==n[len(n)-1]:
            continue
        else:
            (int(n[i])+int(n[i+1]))%2==0
            validity_check.append(1)
    else:
        validity_check.append(0)
print(validity_check)

