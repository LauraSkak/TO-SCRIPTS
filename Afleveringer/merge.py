# Laura og Laura's version

def merge(x:list[int], y:list[int]) -> list[int]:
    i=0 #1
    j=0 #1

    z=[] #1

    while i < len(x) and j < len(y): # 7*(n+m)
        if x[i]>y[j]: #4*(n+m)
            z.append(y[j]) #2*(n+m)
            j+=1 #3*(n+m)
        else:
            z.append(x[i]) #2*(n+m)
            i+=1 #3*(n+m)

    if i == len(x) and j != len(y): #8
        z+=y[j:] # minimum 1, maximum n eller m

    else:
        z+=x[i:] # minimum 1, maximum n eller m

    return z

# 16*(n+m)+(n eller m)+11

x=[3,6,7,9,41,64] #1
y=[7,18,33,56,78,99,100,1333] #1

print(merge(x,y))

    
# Cecilie's version

def merge(x: list[int], y: list[int]) -> list[int]:
    i, j = 0, 0
    z = []  
    while i < len(x) and j < len(y):
        if x[i]<y[j]:
            z.append(x[i])
            i+=1
        else:
            z.append(y[j])
            j+=1
    if i==len(x):
        z=z+y[j:]
    else:
        z=z+x[i:]
    return z