# largest number in the arrray

arrr =[2, 4, 5, 25, 265, 2, 533, 23, 54]


def second_lar(arrr):
    max = arrr[0]
    loc = arrr[0]
    for i in range(0,len(arrr)): # Have to use range function len function is not iterable
        if arrr[i] > max:
            max = arrr[i]
            loc = i
    arrr.pop(loc) # removing te largest number
    max = arrr[0]
    for i in range(0,len(arrr)):
        if arrr[i] > max:
            max = arrr[i]
    return max



def lar(arr):
    max = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


print("Largest number: ", lar(arrr))
print("Second largest number:", second_lar(arrr))