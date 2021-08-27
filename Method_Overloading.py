# Method Overloading


#1. Write two methods with the same name but different number of parameters of same type and call the methods 

class Myclass:
    def sum(self, a=None, b=None, c= None):
        if a!=None and b!=None and c!=None:
            s= a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s='provide at least two numbers'
        return s
obj =Myclass()
print(obj.sum(10,20,30))
print(obj.sum(10,20))
print(obj.sum())


#2. Write two methods with the same name but different number of parameters of different data type and call the methods

import random

class Outcome:
    def __init__(self, value, name):
        self.value = value
        self.name = name
    def __str__(self): return self.name
    def __eq__(self, other):
        return self.value == other.value

Outcome.WIN = Outcome(0, "win")
Outcome.LOSE = Outcome(1, "lose")
Outcome.DRAW = Outcome(2, "draw")
#3. Write two methods with the same name and same number of parameters of same type 



def add(datatype, *args):

	if datatype =='int':
		answer = 0

	if datatype =='str':
		answer =''

	for x in args:
		answer = answer + x

	print(answer)


add('int',5, 6)


add('str', 'Hi ', 'Geeks')
