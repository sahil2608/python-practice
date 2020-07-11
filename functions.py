import random
from random import shuffle, randint
for num in range(5):
    print(num) #from 0 to tis number
for i in range(4,17,2): #(start,end,gap)
    print(i)

a=list(range(1,10))
print(a)

#ENUMERATE FUNCTION
word = "Batman"
for i in enumerate(word):
    print(i)
for a,b in enumerate(word):
    print(a, b)

#ZIP FUNCTION
list1=[1,2,3,4,5]
list2=["a","b","c","d"]
for i in zip(list1,list2):
    print(i)

#IN function
c="s" in "school"
print(c)

print(1 in list1)

shuffle(list1)
print(list1)
print(randint(1,324))



def wish(name="sahil"):
    print("Happy ", name)

wish("dx")


def function(*args): # we can use any variable insted of args
    return sum(args)


print(function(23,4525,5562,65323,6,1))

def funt(**kwargs):
    if "flower" in kwargs:
        print("for you {}".format(kwargs["flower"]))
    else:
        print("No flower")
