# Merging sorted lists

This project is about merging two sorted lists x and y. It relates to the exercise "Merging" in the exercises for week 3 (Introduction to algorithms) and week 4 (Algorithmic efficiency). The project must be done in groups of 2-4 students. Hand in via BrightSpace before Sunday, Oct 1, 23:59
To hand in via BrightSpace, you must enrolled in a group (you will get instructions from Johan at a TA session) and the group must upload their answers as a pdf file (the option to hand in will not be available until groups are formed). Assignment can be found here.

## Problem:

### Question 1: Argue why the merging approach sketches in the exercises for week 3 creates the correct z list and why it terminates.

*We are working with two lists that we know are sorted and of limited size. Therefore,  we know that a while loop where we add a count of one to either j or i for every loop, we will eventually reach the end of one list. By testing whether x[i] or y[i] is larger than the other, you make sure that the numbers in the z list will be in the correct order Once we have reached the end of one list we can add the remainder of the other list. So the algorithm will terminate and produce the correct z list.*

### Question 2: Show that you can merge two sorted lists of size n and m, respectively, into one sorted list containing the elements from the two, in time O(n+m).

*We create a while loop that in the worst case has to go through all values in each list n and m. This would happen in the case where the two largest values would be the last values in the lists n and m. All other operations than the while loop require 1 primitive operation and therefore do not contribute to the O time. Therefore, the computational time can be reduced to O(n+m).*

### Question 3: Implement the merging approach in Python as described on https://github.com/birc-ctib/merging

```python
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
```

## Handin

You must handin a pdf file with your answers to questions 1 and 2, and a py file your Python implementation of merging. 