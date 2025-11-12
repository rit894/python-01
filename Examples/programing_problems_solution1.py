while True:
    x=input('please enter q if you are the last person in the line : ')
    if x=='q':
     
        break
        
    else:
        votingIntrest=input('whom would you like to cast your vote :  \n' \
        'can1 \n' \
        'can2 \n' \
        'can3 ').strip().lower()
        can1=can2=can3=0
        if votingIntrest=='can1':
            can1+=1
        elif votingIntrest=='can2':
            can2+=1
        elif votingIntrest=='can3':
            can3+=1

print("===reaults====")
if can1>can2 and can1>can3:
    print('candidate 1 is winner')
elif can2>can1 and can2>can3:
    print('candidate 2 is winner')
elif can3>can1 and can2>can2:
    print('winner is candidate 3')