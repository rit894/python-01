flowers={'hibiscus':{
     'unit price':100,
     ' no of colours available':6,
     'colours avialable':'Red,white,pink,violet,orange,yellow'},

     'rose':{
     'unit price':200,
     ' no of colours available':4,
     'colours avialable':'Red,white,maroon,yellow'},

     'marigold':{
     'unit price':50,
     ' no of colours available':2,
     'colours avialable':'orange,yellow'},

     'dahlia':{
     'unit price':150,
     ' no of colours available':3,
     'colours avialable':'Red,white,pink'},

     'lotus':{
     'unit price':300,
     ' no of colours available':3,
     'colours avialable':'blue, pink,yelow'}


}
q1='which flower has maximun clour variation?'
q2='choosing colour and getting to know its clour shades '
q3='billing of the flowers '
q4='unique colours'
menu=input(f'chosse among the following questions \nif yes please enter coresspondingly\n{q1}(y)\n{q2}(y1)\n{q3} (y2)\n{q4}(y3)')
print(menu)
if menu=='y':
   if flowers['hibiscus'][' no of colours available']>flowers['rose'][' no of colours available'] and flowers['hibiscus'][' no of colours available']>flowers['marigold'][' no of colours available'] and flowers['hibiscus'][' no of colours available']>flowers['dahlia'][' no of colours available'] and flowers['hibiscus'][' no of colours available']>flowers['lotus'][' no of colours available']:
       print('hibiscus has maximum colour variation')           