# Inheritance

class Animal:  
    def speak(self):  
        print("Animal Speaking")  
 
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  

class DogChild(Dog):  
    def eat(self):  
        print("Eating bread...")  
d = DogChild()  
d.bark()  
d.speak()  
d.eat()  


# method overriding


class Parent():
	
	
	def __init__(self):
		self.value = "Inside Parent"
		
	# Parent's show method
	def show(self):
		print(self.value)
		
# Defining child class
class Child(Parent):
	
	# Constructor
	def __init__(self):
		self.value = "Inside Child"
		
	# Child's show method
	def show(self):
		print(self.value)
		
		
# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()


#Polymorphism with Inheritance: 


class Bird:
    def intro(self):
        print("There are many types of birds.")
	
    def flight(self):
	    print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
	    print("Sparrows can fly.")
	
class ostrich(Bird):
    def flight(self):
	    print("Ostriches cannot fly.")
	
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()


