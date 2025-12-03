word = input("Enter a word: ")
newword = ""

for i in range(len(word) - 1): 
    if word[i] != word[i + 1]:
        newword += word[i]

newword += word[-1]

print("After removing consecutive duplicates:", newword,'hi')


