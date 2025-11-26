''' In Computer Graphics, a display resolution is often represented as a tuple of (width, height). When
 a user changes their monitor settings or when an image needs to be resized, these dimensions must be
 scaled up or down.
 Write a function called scale
 resolutions. It accepts:
 • Alist of tuples, where each tuple represents a resolution (e.g., (1920, 1080)).
 • Ascaling factor (a float, e.g., 0.5 for half size).
 The function should return a new list of tuples where each dimension is multiplied by the scaling
 factor and converted to an integer.'''
def Scale_resolutions(list_tuple_values,scaling_factor):
     
     N=int(input())

     for i in range(N):
          tuple1=[]
          width=int(input())
          height=int(input())
          tuple1.append(width/scaling_factor)
          tuple1.append(height/scaling_factor)
          list_tuple_values.append(tuple(tuple1))

     print(list_tuple_values)

resolutions=[]
factor=float(input())

Scale_resolutions(resolutions,factor)
          