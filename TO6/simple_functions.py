from math import sqrt

#Exercise: Write a function that takes three numbers as arguments and return their product.
def product(x,y,z):
    return x*y*z

#Exercise: Change the function so it only takes one argument, get another from the global scope, and assigns to a local variable for the last value.

def product02(x):
    y=2
    return x*y*z
z=2
#print(product02(2))

#Exercise: Write a function that takes two lists as its input and return the longest of the two.

def longest(x,y):
    if len(x)>len(y):
        return x
    else:
        return y

#Exercise: Write a function that computes the distance between two points.

def distance(x,y):
    return sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
#x=(1,5)
#y=(3,6)
#print(distance(x,y))

    
