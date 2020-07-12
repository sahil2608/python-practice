#Map function
print('Map Function')
def square(a):
    return a*a
list_num=[5,7,8,9,12]
list2=map(square,list_num)
for i in list2:
    print(i)

def len_char(c):
    return len(c)
list_char=["sahil","Liverpool","Authority"]
for i in map(len_char,list_char):
    print(i)

#filter function return only boolean value
print('Filter Function')
def even(a):
    if a%2 == 0:
        return a
joint=[even, square]
print("Even number in list",list(filter(even ,list_num)))
for i in range(1,6):
    print(list(map(lambda x: x(i),joint)))

#lambda function
print('Lambda function')
cube = lambda n : n*n*n
print(cube(3))
print(list(map(lambda  a : a**4, list_num)))
print('Using lambda function in filter function')
print(list(filter(lambda a : a%2 == 0, list_num)))

print('Using lambda function in Map function')
print(list(map(lambda a : a*a*a, list_num)))

#REduce function
from functools import reduce
print(reduce(lambda x,y : x+y, list_num))
#reduce() is a bit harder to understand than map() and filter(), so let's look at a step by step example:

#We start with a list [2, 4, 7, 3] and pass the add(x, y) function to reduce() alongside this list, without an initial value

#reduce() calls add(2, 4), and add() returns 6

#reduce() calls add(6, 7) (result of the previous call to add() and the next element in the list as parameters), and add() returns 13

#reduce() calls add(13, 3), and add() returns 16

#Since no more elements are left in the sequence, reduce() returns 16