import os

class Robot():
    def __init__(self,name,weight,color):
        self.name = name
        self.weight = weight
        self.color = color

    def introduce_self(self):
        print("my name is " + self.name)


class Person():
    age=30
    def __init__(self,n,p,i):
        self.name = n
        self.personality = p
        self.is_sitting = i

    #Dunder method explaining how should print the class itself
    def __repr__(self):
        return f"Person(n:{self.name},p:{self.personality},i:{self.is_sitting})"

    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument, must be int")

        self.name = self.name * x

    def __call__(self,y):
        print("called this function",y)

    def __len__(self):
        return len.self.name

    @staticmethod
    def isAdult(age):
        return age >= 18

    def sit_down(self):
        if self.is_sitting == True:
            print(self.name + " è già seduto")
        else:
            self.is_sitting = True
            print(self.name + " si è seduto")

    def sit_up(self):
        if self.is_sitting == False:
            print(self.name + " è in piedi")
        else:
            self.is_sitting = False
            print(self.name + " si è alzato")

    @classmethod
    def get_age(cls):
        return cls.age


class Dependent(Person):
    def __init__(self, job, firm, n, p, i):
        super().__init__(n, p, i)
        self.job = job
        self.firm = firm

    def cv(self):
        print(f"my name is {self.name} and i'm currently working for {self.firm}")
    def isEmployed(self):
        return True

#Creating a class with metaclass
class Meta(type):
    #userò il metodo dunder __new__ per creare una classe via type
    #def __new__(cls, *args, **kwargs):
    def __new__(self,class_name, bases, args):
        print(args)
        #uppercase attributes
        a = {}
        for name,value in args.items():
            if name.startswith("__"):
                a[name] = value
            else:
                a[name.upper()] = value
        print(a)
        return type(class_name,bases,a)

#la invochiamo con una definizione di classe da metaclasse
class Dog(metaclass=Meta):
    x = 10
    y = 5
    nome = 'carlino'

    def hello(self):
        print('hi')

d = Dog()
#ora è in maiuscolo un elemento
print(d.X)





r1 = Robot(name="tom",weight=30,color="Blue")
r2 = Robot(name="Jack",weight=40,color="Red")
p1 = Person(n='lisa',p='psycho',i=True)
print(p1)
p1*4
print(p1)
p1.sit_down()
p1.get_age()

p3 = Dependent(n='lisa',p='psycho',i=True,job='Data Scientist', firm='Gft')
p3.cv()
p3.sit_up()
p3.isEmployed()





r1 = Robot(name="tom",weight=30,color="Blue")
r2 = Robot(name="Jack",weight=40,color="Red")


p3.owned_robot = r1
p3.owned_robot.introduce_self()

