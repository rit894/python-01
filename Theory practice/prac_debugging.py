import pdb 
def my_func(x,y):
    result=x+y 
    pdb.set_trace()
    return result
print(my_func(3,4))