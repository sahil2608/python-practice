#Immuteable = can't be changed

cooordinates =[(4,2),(7,98)]
#cooordinates[1]= 1    can't do it
print(cooordinates[1])

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2>=num2 and num2>= num3:
        return num2
    else:
        return num3

print(max_num(14,78,74))


def cal(num1, op, num2):
    if op == "+":
        print(num1+num2)
    elif op == "-":
        print(num1-num2)
    elif op == "/":
        print(num1/num2)
    elif op == "*":
        print(num1*num2)
    else:
        print("Invalid operator")

#num1 = float(input(print("Enter num 1 "))) use of printe will print none

num1 = float(input("Enter num 1 "))
op = input("Enter operator ")
num2 = float(input("Enter num 2 "))
cal(num1, op, num2)