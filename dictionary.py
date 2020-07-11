monthConversions = {
    "jan": "january", # No duplicate
    "feb": "february",
    "jun": "june"
}
print(monthConversions["jun"])
print(monthConversions.get("junl", "Not a valid")) #a default value if there is nothing
friends = ["carl", "david", "cook"]

i=1
while i <= 3:
    print("Boom")
    i+=1

for friend in friends:  #the word with form is printed with statement
    print(friend)

for index in range(2,9):  #print number from 2 to 9
    print(index)

for index in range(len(friends)):   # print friends in  array
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First")
    elif index == 4:
        print("last")
    else:
        print("HAhAhAhAha")