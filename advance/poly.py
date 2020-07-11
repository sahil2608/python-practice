#polymorphism

class Dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(self.name , " says WooF")

class Cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(self.name, " says MeoW")

my_dog=Dog('Max')
my_cat=Cat("Caroline")

my_cat.speak()
my_dog.speak()

for i in [my_cat,my_dog]:
    print(type(i))
    print("For loop")
    i.speak()

def pet_speak(pet):
    print(type(pet))
    pet.speak()

pet_speak(my_dog)
pet_speak(my_cat)

#Abstract classes
class Document():
    def __init__(self,name):
        self.name = name
    def show(self):
        raise NotImplementedError("Atleast implement sub abstract method ")
my_doc=Document('Pdf')

class Pdf(Document):
    def show(self):
        print("Pdf content here")

class Word(Document):
    def show(self):
        print("Word content here")

my_pdf=Pdf('pdf')
my_word=Word('word')
my_pdf.show()
my_word.show()