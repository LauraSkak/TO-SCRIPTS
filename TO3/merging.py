x=[3,6,7,9,41,64] #1
y=[7,18,33,56,78,99,100,1333] #1
z=[] #1

i=0 #1
j=0 #1

while i < len(x)-1 and j < len(y)-1: #m+n
    if x[i]>y[j]: 
        z.append(y[j]) #1
        j+=1 #1
    else:
        z.append(x[i]) #1
        i+=1 #1

if i == len(x)-1:#1
    z+=y[j:] #1

else: #1
    z+=x[i:] #1

print(z) #1

#3*(m+n)+10
#reduceres to O(m+n)


#Funktion:

def merge(x:list[int], y:list[int]) -> list[int]:
    i=0
    j=0

    z=[]

    while i < len(x)-1 and j < len(y)-1:
        if x[i]>y[j]: 
            z.append(y[j])
            j+=1
        else:
            z.append(x[i])
            i+=1

    if i == len(x)-1:
        z+=y[j:]

    else:
        z+=x[i:]

    return z

print(merge(x,y))

    
