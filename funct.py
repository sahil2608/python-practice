def intros(name):
    print("Yo! " + name)

intros("sahil")

def cube(num):
    return num*num*num
#nothing can be worked after return statement
print(cube(5))

is_male = True
is_tall = False

if not(is_male) or is_tall:   #use and for both a condition
    print("Male or tall")
elif is_male and is_tall:   #else if
    print("Short")
else:
    print("Really")
x = lambda a,b: a*b
print("Lambda function: ", x(45,12))