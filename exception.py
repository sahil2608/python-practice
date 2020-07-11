try:
    num = int(input("Enter the number: "))
    print(num)
except:
    print("Invalid input")

try:
    G = 12/0
    num = int(input("Enter the number: "))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")