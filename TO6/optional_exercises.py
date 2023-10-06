#Exercise: A DNA string consists of A, C, G, and T letters. Write a function that counts how many times each of the letters occur in a string, but raises an exception if there is a letter that isn’t one of these four.
def base_count(x):
    base_dict={}
    for i in range(len(x)):
        if x[i] not in ['A','C','G','T']:
            raise Exception("Not a valid base", x[i])
        if x[i] not in base_dict:
            base_dict[x[i]]=0
        base_dict[x[i]]+=1
    return base_dict

#print(base_count('ABCTA'))

#exercise 2
def raises_error(x):
    if x < 0:
        raise Exception("Negative", x)
    if x > 0:
        raise Exception("Positive", x)
    return 42

def f(x):
    return raises_error(x)

def g(x):
    try:
        print(f(x))
    except Exception as e:
        if e.args[0] == "Negative":
            print("g:", e.args[0])
            return f(0)
        else:
            raise

#print(g(-1)) = g: Negative, 42
#print(g(-1))

#print(g(1)) = g: Exception ('Positive', 1)
#print(g(1))

try:
    #print(g(-1))
    #print(g(-3))
    print(g(1))
    print(g(-1))
except Exception as e:
    #print(e)
    print("Outer", e.args[0])

#Parameterised insertion sort
#Exercise: Go through the code and make sure you understand why it sorts in increasing and decreasing order.
