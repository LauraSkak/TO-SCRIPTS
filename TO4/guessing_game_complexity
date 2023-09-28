# Exercise: Identify the best- and worst-case scenarios for each strategy and derive the best-case and worst-case time usage.

# 1. Best case er at man rammer første gang. Det sker, hvis svaret er 1. O(1)
# Worst case er at man først rammer ved 20. O(n) (n=listens længde)

# 2.Best case er at man rammer første gang (20). O(1)
# Worst case er at man først rammer ved 1. O(n) (n=listens længde)

# 3.Best case er at man ramme første gang. O(1)
# Worst case, er at man rammer efter 5 gange. O(log(n))

def input_selection(prompt: str, options: list[str]) -> str:
    """Get user input, restrict it to fixed options."""
    modified_prompt = "{} [{}]: ".format(
        prompt.strip(), ", ".join(options)
    )
    while True:
        inp = input(modified_prompt)
        if inp in options:
            return inp
        # nope, not a valid answer...
        print("Invalid choice! Must be in [{}]".format(
            ", ".join(options)
        ))


print("Please thing of a number from 1 to 20, both included.")
print("Let me know how good my guess is.\n")

#Vores funktion:

top=20 #1
bottom=1 #1
guess=round(top/2) #4 => 1

for i in range(20): #n
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"]
    ) #1n
    if result == "hit": #3n
        print("Wuhuu!") #1
        break #1
    
    if result == "low": #1n
        bottom=guess+1 #3
        guess=round(bottom+(top-bottom)/2) #9
    
    if result == "high": #3n
        top=guess-1 #3
        guess=round(bottom+(top-bottom)/2) #9
        

    print("I must have been too low, right?", result) #1 

=