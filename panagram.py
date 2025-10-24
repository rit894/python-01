'''A pangram is a sentence that contains every letter of the English 
alphabet at least once. Write a program to check whether a given 
sentence is a pangram'''




# Step 1: Read input and convert to lowercase
sentence = input("Enter a sentence: ").lower()

# Step 2: Create a list of all alphabet letters
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# Step 3: Create a list to track unique letters found
found_letters = []

# Step 4: Loop through each character in the sentence
for char in sentence:
    if char in alphabet and char not in found_letters:
        found_letters.append(char)

# Step 5: Check if all 26 letters are found
if len(found_letters) == 26:
    print("The entered sentence is a pangram")
else:
    print("The entered sentence is not a pangram")

