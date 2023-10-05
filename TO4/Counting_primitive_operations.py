accumulator = 0 #1
for n in numbers: #n (bogen siger 5n+2)
 accumulator += n #3n
mean = accumulator / len(numbers) #4
#=3n+5 (LS:4n+5) => O(n) #laura please explain why 4n+5


accumulator = 0 #1
length = 0 #1
for n in numbers: #n
 accumulator += n #3
 length += 1 #2
mean = accumulator / length #4
#=5n+6 (LS: 6n+6) => O(n)

