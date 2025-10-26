originalMSG=input("Enter the message to be encoded: ")
corruptMSG=""
couurptCount=0
totalcount=0
for char in originalMSG:
    if char in 'qwertyuiopasdfghjklzxcvbnm':
        corruptMSG+=chr(ord(char)-32)
        couurptCount+=1
        totalcount+=1
    elif char in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        corruptMSG+=chr(ord(char)+32)
        couurptCount+=1
        totalcount+=1
    else:
        corruptMSG+=char
        totalcount+=1
print("The encoded message is:",corruptMSG)
percentCorrupt=(couurptCount/totalcount)*100
print("the courrtpion percentage is ", round(percentCorrupt,2),"%")
