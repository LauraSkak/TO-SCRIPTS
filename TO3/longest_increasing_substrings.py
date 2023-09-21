x = [12, 45, 32, 65, 78, 23, 35, 45, 57]
list_of_substrings=[]
substring=[x[0]]

for i in range(1,len(x)):
    if x[i]>substring[-1]:
        substring.append(x[i])
    else:
        list_of_substrings.append(substring)
        substring=[x[i]]

list_of_substrings.append(substring)
#substring=[x[i]]

longest_substring=[]

for i in range(len(list_of_substrings)):
    if len(longest_substring)<len(list_of_substrings[i]):
        longest_substring=list_of_substrings[i]

#print(list_of_substrings)
print(longest_substring)