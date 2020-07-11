#Strings are IMMUTABLE!
print("\"Really\" \n sahil") #To print Quotation mark" use \" and new line \n
phrase = "Liverpool \tFc"
print(phrase*2)
print(phrase.upper()) # to convert into upper
print(phrase.lower())
print(phrase.isupper()) # To check if upper case
print(phrase.islower())
print(phrase.upper().isupper()) #use 2 diffrent classes
print(len(phrase)) # length of string
print(phrase[2]) #Specfic character in string
print(phrase.index("F"))
print(phrase.index("oo")) # find the string
print(phrase.replace("Fc", "Club"))
print(len(phrase))
pul = phrase[9:]
print("Real Madrid "+ pul)
#.Format method
print("MY fav club is {}".format(phrase))
print(f"MY fav club is {phrase}")

print("MY name is {} Chhikara".format("Sahil"))
print("colour {0} {2} {1}".format("Red", "greeeen", "Blue"))
print("colour {b} {r} {g}".format(r="Red", g= "greeeen", b= "Blue"))

#float formatting method part of .format method
#"{value:width.precisionf}"
pie = 22/7
print("Value is {}".format(pie))
print("Value is {p:1.3f}".format(p=pie)) #p:1.3f tell that print 3 value after decimal and 1 is whitespaces


