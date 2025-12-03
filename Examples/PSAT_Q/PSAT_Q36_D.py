def encrypt(a):
 list1=[]
 alphabets= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 for char in a:
  for i in range(len(alphabets)):
    if alphabets[i]==char :
      if (i+1) % 2==0:
        list1.extend(['!'*(i+1)])
      elif (i+1) % 2 !=0:
        list1.extend(['@'*(i+1)])
 list1=''.join(list1)
 print(list1)
encrypt('AB')

