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

#filter function
print('Filter Function')
def even(a):
    if a%2 == 0:
        return a
print(list(filter(even ,list_num)))


#lambda function
print('Lambda function')
cube = lambda n : n*n*n
print(cube(3))
print(list(map(lambda  a : a**4, list_num)))
print('Using lambda function in filter function')
print(list(filter(lambda a : a%2 == 0, list_num)))

print('Using lambda function in Map function')
print(list(map(lambda a : a*a*a, list_num)))