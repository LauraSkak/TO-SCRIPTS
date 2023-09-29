x = [5,6,3,4,2,4,2,3,4]

m = 5

buckets = [0]*m

print(buckets)

for key in x:
	buckets[key] += 1
result = []
for key in range(m):
	for i in range(buckets[key]):
		result.append(key)