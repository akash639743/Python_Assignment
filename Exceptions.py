# Exceptions


#Arithmetic Exception without exception handling

try:
	a = 10/0
	print (a)
except ArithmeticError:
		print ("This statement is raising an arithmetic exception.")
else:
	print ("Success.")


# Arithmetic exception using try-catch block


# Python code to illustrate
# working of try()
def divide(x, y):
	try:
		# Floor Division : Gives only Fractional Part as Answer
		result = x // y
		print("Yeah ! Your answer is :", result)
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(3, 2)


#The method in main class without try block

try:
	number1=100
	number2=10
	quotient = number1/number2
	
	data = "Selftutus"
	mylist = [1,2,3,4]
	print(mylist[20])
	print("Quotient is {}".format(quotient))
except ZeroDivisionError:
	print("division by zero is being performed")
except AttributeError:
	print("Attribute error occurred")
except IndexError:
	print("Index out of range")





#Throw exception with your own message

class Error(Exception):
	pass
class dobException(Error):
	pass

year = int(input("Enter the year of Birth"))
age=2021-year
try:
	if age<=30 & age>20:
		print("THe age is valid. You can apply for the exams")
	else:
		raise dobException
except dobException:
	print("The year age is not valid. you cannot apply for the exams" )



# # # # Python program to demonstrate finally

# No exception Exception raised in try block
try:
	k = 5//0 # raises divide by zero exception.
	print(k)

# handles zerodivision exception	
except ZeroDivisionError:
	print("Can't divide by zero")
	
finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')






#Program with finally block

try:
    print("try")
except ZeroDivisionError:
    print("Except")
finally:
    print("finally")

try:
    print("try")
    print(10/0)
except ZeroDivisionError:
    print("Except")
finally:
    print("finally")




#Generate FileNotFoundException

try:
    #trying to open a file in read mode
    fo = open("newfilee.txt","rt")
    print("File opened")
except FileNotFoundError:
    print("File does not exist")  #FileNotFoundException
except:
    print("Other error")





try:  
    a = int(input("Enter a:"))   
    b = int(input("Enter b:"))    
    c = a/b  
except:  
    print("Can't divide with zero") 



#Generate Arithmetic Exception

try:
	a = 10/0
	print (a)
except ArithmeticError:
		print ("This statement is raising an arithmetic exception.")
else:
	print ("Success.")


#Generate IOException

try:
	f=open ("newfile.txt")
	f.write("my name is")
except IOError:
	print("the is incorrect")
else:
	print("this is correct")


