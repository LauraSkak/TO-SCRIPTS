s=["a","b","c"]

ps=[]
sub_ps=[]

# for i in range(len(s)+1):
#     print(i)
#     for j in range(i):
#         for l in range(len(s)):
#             for k in range(len(s))
#             sub_ps.append(s[l])
#             print(sub_ps)
    
#     ps.append(sub_ps)


# print(ps)

# for l in range(len(s)+1):
#     print(l)
#     for i in range(len(s)):
#         print(i)

# for i in range(len(s)):
#     for j in range(i,len(s)):
#         print(i,j)

# def powerset(s):
#     result=[[]]
#     for x in s:
#         result += [subset+[x] for subset in result]
#         print(result)
#     return result

# print(powerset(s))

result=[[]]
for i in range(len(s)):
    for j in range(len(result)):
        result.append(result[j]+[s[i]])
print(result)