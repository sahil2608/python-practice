num_luck = [28,56,89,45,75,15,35]
friends = ["carl", "david", "cook", 2, 2.45]
a=type(friends)
print(a)
num_luck.sort()
#friends.sort() only if all values of same type
print(friends[2])
print(friends[-2])
print(friends[1:]) #print after starting specfic [ositon
print(friends[1:3])
friends[1]="Mike" #modify list
print(friends.index("Mike")) #if a element exist
print(friends.count("Mike"))
friends.append("Saghiol") #add value in the liste
print(friends)
friends.extend(num_luck)
friends.pop() #remove last list
print(friends)
friends.insert(2, "reeeeeeohit")
print(friends)
friends.remove(2)

print(friends)
friends.clear()

hall= friends.copy()
print(hall)


