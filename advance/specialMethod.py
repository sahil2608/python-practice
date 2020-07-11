from areaoftriangle import areaOfTriangle
print(areaOfTriangle(6,8,10))
#using method from other file

#special method - Using Builtin method with class

class Example():{}

exm = Example()
print(exm) # this will print address
#print(len(exm)) this will produce error

class Account():
    def __init__(self, owner, acc_num, amount):
        self.owner=owner
        self.acc_num=acc_num
        self.amount=amount


my_account = Account("Sahil", 25541224, 2343)
print(len(my_account.owner))
print("Owner: ",my_account.owner,", Account number:", my_account.acc_num,", Amount $ ", my_account.amount)
del my_account
# this will show error because my_account is deleted
# print(my_account.owner)