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

print(reversed)

if reversed:
    midtpoint = len(n)//2
    for i in range(midtpoint):
<<<<<<< HEAD
        n_ordered.insert(i, n[i])
        n_ordered.insert(i, n[(len(n)-1-i)])
    if len(n)%2 != 0:
        n_ordered.insert(midtpoint, n[midtpoint]) 

print(n_ordered)
=======
        print(n)
        print(i, -(1+i))
        n[i], n[-(1+i)] = n[-(1+i)], n[i]
print(n)
>>>>>>> e169cf4a8468729ffee2eee9f3c4ed8dd370cfbd
