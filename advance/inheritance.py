#inheritance
class Sports():
    def __init__(self):
        print("Get ready")
    def excitement(self):
        print('Excited')
    def start(self):
        print("It's time to get started")
my_sports = Sports()
my_sports.start()
my_sports.excitement()

class football(Sports): #Inhetrited sports in football
    def __init__(self):
        Sports.__init__(self)
        print("Time for football")
    def league(self):
        print("Mo salah")
    def excitement(self):
        print("Time to score goals")

liver = football()
liver.__init__()
liver.start()
liver.excitement()