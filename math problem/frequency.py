# finding the frequency of each element

arr1 = [1, 2,   8,  3,   2,   2,   2,   5,  1]
fr = [None] * len(arr1) #acreating an empty list to add the no of times a element appear
visited = -1

for i in range(0,len(arr1)):
    count =1
    for j in range(i+1,len(arr1)):
        if arr1[i] == arr1[j]:
            count += 1
            fr[j] = visited # so that it won't count it again
    if fr[i] != visited:
        fr[i]=count

for i in range(0,len(arr1)):
    if fr[i] != visited:
        print("Element in array:", arr1[i], " No of times: ", fr[i])
