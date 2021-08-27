

import abc
from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self): #Abstractmethod
        pass
    def show(self):
        print("concrete Method") #Non-abstract methods

class Child(Father):   # Child Class
    
    def disp(self):
        print("Child Class")
        print("Defining Abstract Method")

c=Child()

c.disp()
c.show()

class Document(ABC):
    

    @abstractmethod
    def display(self):
        pass


class PDFDocument(Document):
        
     def display(self):
         print("display self.content as PDF Document")

class WordDocument(Document):
    def display(self):
        print("display self.content as Word Document")


file1 = PDFDocument()
file1.display()

file2 =WordDocument()

file2.display()


# Instantiation

from abc import ABC,abstractmethod

class Animal(ABC):
	@abstractmethod
	def move(self):
		pass
class Human(Animal):
	def move(self):
		print("I can walk and run")

class Snake(Animal):
	def move(self):
		print("I can crawl")

class Dog(Animal):
	def move(self):
		print("I can bark")

class Lion(Animal):
	def move(self):
		print("I can roar")

c=Lion()
c.move()




