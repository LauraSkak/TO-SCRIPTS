def merge(x:list[int],y:list[int]) ->list[int]:
    i=0
    j=0
    z=[]
    while i<len(x) and j<len(y):
        if x[i]<y[i]:
            z.append(x[i])
            i+=1
        else:
            z.append(y[j])
            j+=1
        print(z)
    if i==len(x):
        z=z+y[j:]
    else:
        z=z+x[i:]
    return z

x=[1,2,4,6]
y=[1,3,4,5]
print(merge(x,y))

#Cecilies kode

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