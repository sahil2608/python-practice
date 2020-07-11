from Student import Student
a,b,c=3,3,4
char_name = "Sahil"
char_age = 22.122
ismale = True
print("My name is " + char_name)
print("my age is " , char_age)
char_name = "hit"
print("not mine is " + char_name)
print(ismale)
print(char_age)
print(a , b , c)

student1 = Student("jim", "Arts", 3.2, False)
student2 = Student("jimmy", "Arts", 4.2, False)
print(student1.on_honour_roll())
