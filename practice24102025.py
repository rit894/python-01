'''A pangram is a sentence that contains every letter of the English 
alphabet at least once. Write a program to check whether a given 
sentence is a pangram'''

sentence = input("Enter a sentence: ").lower()
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z" ]
sentenceword=[]
for char in sentence:
    if char in alphabet:
      sentenceword.append(char)
      if char in sentenceword:
         continue
    if sentenceword == alphabet :
      print("The entered sentence is a pangram")
      break
    else:
      print("The entered sentence is not a pangram")
      break
       
