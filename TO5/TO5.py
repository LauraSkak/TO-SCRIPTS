# Laura N's kode 

# n=[9,8,7,6,5,4,3,2,1]
# n_ordered=[]
# reversed=False

# if reversed == False:
#     midtpoint = len(n)//2
#     for i in range(midtpoint):
#         print(i)
#         n_ordered.insert(i, n[i])
#         n_ordered.insert(i, n[(len(n)-1-i)])
#         print(n_ordered)
#     if len(n)%2 != 0:
#         n_ordered.insert(midtpoint, n[midtpoint]) 

#print(n_ordered)

# Laura S's kode 

n=[9,8,7,6,5,4,3,2,1]
n=[2,1]
reversed=True
i = 1

while reversed and i < len(n):

	if n[i-1] < n[i]:
	
		reversed = False

	else:

		i += 1


if reversed:

	midtpoint = len(n)//2
	
	for i in range(midtpoint):

		n[i], n[-(1+i)] = n[-(1+i)], n[i]


# Implementeret i insertion sort

x=[1,5,4,4, 3,2,10,4]
i = 1

while i < len(x): 
    j = i 
    start = i-1
    end = i-1
    
    if i < len(x)-1:
        
        while x[end] >= x[end+1]:
            end += 1

        if end > start:
            midtpoint = start+(end-start)//2
            for k in range(start, midtpoint+1):
                x[k], x[end-(k-1)] = x[end-(k-1)], x[k]
            i = i + (end-start)
    
    while j > 0 and x[j-1] > x[j]:
        x[j-1], x[j] = x[j], x[j-1]
        j -= 1
    
    i += 1
        
        
print(x)


# Implementeret i insertion sort with steps

x=[1,5,4,3,2,10,4]*100

steps = 0
i = 1
steps += 1

while i < len(x): 
    steps += 1
    j = i 
    steps += 1
    start = i-1
    steps += 1
    end = i-1
    steps += 1
    
    if i < len(x)-1:
        steps += 1
        while x[end] >= x[end+1]:
            steps += 1
            end += 1
            steps += 1

        if end > start:
            steps += 1
            midtpoint = start+(end-start)//2
            steps += 1
            for k in range(start, midtpoint+1):
                steps += 1
                x[k], x[end-(k-1)] = x[end-(k-1)], x[k]
                steps += 1
            i + (end-start)
            steps += 1
    
    while j > 0 and x[j-1] > x[j]:
        steps += 1
        x[j-1], x[j] = x[j], x[j-1]
        steps += 1
        j -= 1
        steps += 1
    
    i += 1
    steps += 1
        
       
#print("steps", steps)


x=[1,5,4,3,2,10,4]*100

steps = 0
steps += 1

for i in range(1,len(x)):
    steps += 1
    j = i
    steps += 1
    while j > 0 and x[j-1] > x[j]: 
        steps += 1
        x[j-1], x[j] = x[j], x[j-1]
        steps += 1
        j -= 1
        steps += 1

#print("steps", steps)