# Shifting elements left in array

arr1 =[2, 4, 5, 25, 265, 2, 533, 23, 54]
print("List: ", arr1)
for i in range(0, 2):
    first = arr1[0]
    for j in range(0, len(arr1)-1):
        arr1[j] = arr1[j+1]

    arr1[len(arr1)-1] = first


print("Reversed list: ", arr1)
