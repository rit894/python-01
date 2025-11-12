word="a12rwho55ehjt6hyt7ju6tnt4"
num=[x for x in range (10)]
newword=""
for char in word:
    if char in str(num):
        continue
    else:
        newword+=char
print(newword)
