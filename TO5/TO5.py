n=[9,8,7,6,5,4,3,2,1]
n_ordered=[]
reversed=False

if reversed == False:
    midtpoint = len(n)//2
    for i in range(midtpoint):
        print(i)
        n_ordered.insert(i, n[i])
        n_ordered.insert(i, n[(len(n)-1-i)])
        print(n_ordered)
    if len(n)%2 != 0:
        n_ordered.insert(midtpoint, n[midtpoint]) 

print(n_ordered)