from math import *
my_num = 25
num = -2
print(str(my_num) + " Chilll")
print(sum([7,8]))  # Only two variables possible and Square brackets
print(abs(num)) # Absolute number
print(pow(3,2)) # power
print(max(6,25,56,35,56))  # min number
print("Min",min(9,25,56,35,56)) # max number
print(round(2.45252)) # round off
print("flooer value", floor(3.955)) # current number after point no matter what
print("Ceil value", ceil(3.2155)) # upper number
print("Square of 69",sqrt(69))
print(eval('num + 1'))
print(7**3)  #print the power

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num;
    return result

print(raise_to_power(3,6))

print(bin(2)) # binary values