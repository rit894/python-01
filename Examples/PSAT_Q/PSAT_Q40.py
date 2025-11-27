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

