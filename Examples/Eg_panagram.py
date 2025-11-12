'''A pangram is a sentence that contains every letter of the English 
alphabet at least once. Write a program to check whether a given 
sentence is a pangram'''



sentence = input("Enter a sentence: ").lower()

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

found_letters = []

for char in sentence:
    if char in alphabet and char not in found_letters:
        found_letters.append(char)
if len(found_letters) == 26:
    print("The entered sentence is a pangram")
else:
    print("The entered sentence is not a pangram")
