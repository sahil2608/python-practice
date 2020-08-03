#Python program to check if the given number is a Disarium Number
#A number is said to be the Disarium number when the sum of its digit
# raised to the power of their respective positions becomes equal to the number itself.


def cal_length(n): # to check the length of number
    length = 0
    while n != 0:
        length = length+1
        n = n//10
    return length

n=num=int(input("Enter the number to check"))
len = cal_length(num)
val = rem = 0
while num > 0:
    rem = num%10
    val = val + int(rem**len)
    num = num//10
    len-=1

if val == n:
    print(n, " is Disarium number")
else:
    print(n, " not is Disarium number")
