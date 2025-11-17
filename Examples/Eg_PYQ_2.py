'''The Green Plantation Nursery sells the following five flower plants:- 
1. Hibiscus 
Unit Price: Rs.100, Colours available: Red, White, Pink, Violet, Orange, Yellow 
2. Rose 
Unit Price: Rs.200, Colours available: Red, White, Maroon, Yellow 
3. Marigold 
Unit Price: Rs.50, Colours available: Orange, Yellow 
4. Dahlia 
Unit Price: Rs.150, Colours available: Red, White, Pink 
5. Lotus 
Unit Price: Rs.300, Colours available: Blue, Pink, Yellow 
Store these details using appropriate data organization and answer the following questions 
using a one-time menu option. 
1. Which flower has maximum colour variations? 
2. Given a colour name as input, list the names of flowers which has that colour shade. 
3. Given an amount as input, which all flowers can be bought such that all their colour 
varieties are purchased? 
4. List all unique colours - a colour which is available for only one type of flower. '''

flowers = {
    'Hibiscus': {
        'unit price':100,
         'colours':['red','white','pink','violet','orange','yellow']
    
    },
    'Rose':{
        'unit price':200,
        'colours':['red','white','maroon','yellow']
    },
    'Marigold':{
        'unit price':50,
        'colours':['orange','yellow']

    },
    'Dahlia':{
        'unit price':150,
        'colours':['red','white','pink']

    },
    'Lotus':{
        'unit price':300,
        'colours':['blue','pink','yellow']

    }
}
def max_flower_variations():
    max_count=0
    max_flower=''
    for flower,colour in flowers.items():
     total= (len(colour['colours']))
     if max_count< total:
        max_count=total
        max_flower=flower
    print(max_flower,'is colour with maximum variations.')

def colour_variations(col):
   flowers1=[]
   for flower,colour in flowers.items():
      if col in colour['colours']:
         flowers1.append(flower)
   print(flowers1)
   print('these flowers are avialable in this shade')

def cost_flower(cost):
   flowers1=[]
   for flower,colour in flowers.items():
      if cost==colour['unit price']:
         flowers1.append(flower)
   print(flowers1)
   print('these are avialable for this cost.')
cost=int(input())
cost_flower(cost)

         

   
         
     

