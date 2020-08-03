# Python program to check if the given number is Happy Number
# A number is said to be happy if it yields 1 when replaced by the sum of squares
# of its digits repeatedly. If this process results in an endless cycle of numbers containing 4,
# then the number will be an unhappy number.

def cal_length(n): # to check the length of number
    length = 0
    while n != 0:
        length = length+1
        n = n//10
    return length


def check(num):
    val = rem = 0
    len = cal_length(num)
    while num > 0:
        rem = num%10
        val = val + int(rem**2)
        num = num//10
        len-=1

    if val == 1:
        print("Happy number number")
    elif val == 4:
        print("Not a Happy number")
    else:
        check(val)

check(int(input("Enter a number to check")))