# Using inbuilt reversed function In this function
# we don't copy the list or reverse original list we just iterate in reverse order

arrr = [2, 4, 5, 25, 265, 2, 533, 23, 54]
print("Array", arrr)


def reverse(arrr):
    return [i for i in reversed(arrr)]
# if i do not put i before for it will produce error


print("Reversed list: ", reverse(arrr))

# in this method we change the list
arr1 =[2, 4, 5, 25, 265, 2, 533, 23, 54]
arr1.reverse()
print("Reversed list: ", arr1)

# USING THE slicing technique (copying data into new list)

def rev_li(arrr):
    arr2 = arrr[::-1]
    return arr2


print("Reversed list: ", rev_li(arrr))