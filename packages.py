#                         # PACKAGES




class Employee:
    

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


Akash = Employee("Akash", 255, "Developer")




print(Akash.name,Akash.salary,Akash.role )




# Python code to illustrate the Modules
class Bmw:
	
	def __init__(self):
		self.models = ['i8', 'x1', 'x5', 'x6']

	
	def outModels(self):
		print('These are the available models for BMW')
		for model in self.models:
			print('\t%s ' % model)


class Audi:
	
	def __init__(self):
		self.models = ['q7', 'a6', 'a8', 'a3']

	
	def outModels(self):
		print('These are the available models for Audi')
		for model in self.models:
			print('\t%s ' % model)


class Nissan:
	
	def __init__(self):
		self.models = ['altima', '370z', 'cube', 'rogue']

	
	def outModels(self):
		print('These are the available models for Nissan')
		for model in self.models:
			print('\t%s ' % model)

ModBMW = Bmw()
ModBMW.outModels()


ModAudi = Audi()
ModAudi.outModels()


ModNissan = Nissan()
ModNissan.outModels()



# Python code to illustrate the Modules
class Bmw:
	# First we create a constructor for this class
	# and add members to it, here models
	def __init__(self):
		self.models = ['i8', 'x1', 'x5', 'x6']

	# A normal print function
	def outModels(self):
		print('These are the available models for BMW')
		for model in self.models:
			print('\t%s ' % model)


# Python code to illustrate the Module
class Audi:
	# First we create a constructor for this class
	# and add members to it, here models
	def __init__(self):
		self.models = ['q7', 'a6', 'a8', 'a3']

	# A normal print function
	def outModels(self):
		print('These are the available models for Audi')
		for model in self.models:
			print('\t%s ' % model)


# Python code to illustrate the Module
class Nissan:
	# First we create a constructor for this class
	# and add members to it, here models
	def __init__(self):
		self.models = ['altima', '370z', 'cube', 'rogue']

	# A normal print function
	def outModels(self):
		print('These are the available models for Nissan')
		for model in self.models:
			print('\t%s ' % model)


