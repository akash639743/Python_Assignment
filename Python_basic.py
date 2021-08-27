# Python Basic


# 1. Write a program to print your name.
var= "Akash Negi"
print("My name is ", var)

print("My name is Akash negi")



# 2. Write a program for a Single line comment and multi-line comments.



print("this is a single line comments")   #created simply by beginning a line with the hash (#) character.



'''
multiline comments are created simply by the triple line(''' ''') character.

'''

# 3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.
# Data types
var1=1
print(type(var1)) # it is integer

x=10
y=9
print(x > y)
print(x == y) 
print(type(x>y))
print(type(x==y))  # it is boolen


z=1.1
print(type(z))


num = float(input("Enter any decimal Number  "))
print("Enter any decimal Number  ", num)
print(type(num))



# 4. Define the local and Global variables with the same name and print both variables and
# understand the scope of the variables

z = 25 #global
def func():
    global z
    
    print(z)
    z=20#local
func()
print(z)