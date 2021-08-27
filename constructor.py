# Constructor


'''
1. Write a class with a default constructor, one argument constructor and two argument
constructors. Instantiate the class to call all the constructors of that class from a main
class
'''
class computer():
    def __init__(self):
        print("hello")
    def config(self):
        print("my name is Akash")
c=computer()
c1=computer() # defualt constructor
c.config()


#2. Call the constructors(both default and argument constructors) of super class from a child class

class Father:
    def __init__(self):
        print("Father class Constructor")

    def show(self):
        print("Father class Instance Method")
class Son(Father):
    def __init__(self):
        super().__init__()
        print("son class Constructor")

    def disp(self):
        print("son class Instance")

s= Son()


#3. Apply private, public, protected and default access modifiers to the constructor


#private

class Test:
    def __init__(self):
        self.__a = 20
    def m1(self):
        print("hello",self.__a)
t =Test()
t.m1()


#private

class Test:
    def __init__(self):
        self.a = 20
    def m1(self):
        print("hello")
t =Test()
t.m1()
print(t.a)

#protected

class Test:
    def __init__(self):
        self._a = 20
    def m1(self):
        print("hello")
t =Test()
t.m1()
print(t._a)


#4. Write a program which illustrates the concept of attributes of a constructor.

class Myclass:
    x=19
    def change_class(self,new_x):
        self.x=new_x
new_class= Myclass()
print(new_class.x)
new_class.change_class(100)
print(new_class.x)