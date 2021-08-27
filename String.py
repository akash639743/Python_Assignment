# String


#1. Different ways creating a string


string1 = 'Hello'
print(string1)

string2 = "Hello"
print(string2)

string3 = '''Hello'''
print(string3)


string4 = """Hello, welcome to
           the world of Python"""
print(string4)

#2. Concatenating two strings using + operator
a="Akash "
b="Negi"
print("My name is ",a+b)

#3. Finding the length of the string
c="My name is Akash Negi"
d=len(c)
print("the Length of c :",d)

# 4. Extract a string using Substring

string = "My name is Akash"
print(string[::]) # all print
print(string[:7:2])# print starding to length of 7 with 1 chacator gap

# 5. Searching in strings using index()

string = "My name is Akash"
print(string.index("s"))
print(string.index("A"))


# 6. Matching a String Against a Regular Expression With matches()

import re

line="pet:cat i love cats"
match=re.match(r"pet:\w\w\w",line)
print(match)
print(match.group(0))

# 7. Comparing strings

print("Geek" == "Geek")
print("Geek" < "geek")
print("Geek" > "geek")
print("Geek" != "Geek")


# 8. startsWith(), endsWith() and compareTo()

name="My name is Akash"
print(name.startswith("My"))  #startsWith()


print(name.endswith("is")) # endswith


x=int(input("enter the no."))
y=int(input("enter the no."))

if (x==y):
    print("these are same") # compareTo
else:
    print("these are not same")


# 9. Trimming strings with strip()

name="     Akash       "
print(name.strip())


# 10. Replacing characters in strings with replace()


name="My name is Akash"
print(name.replace('Akash',"akki"))



# 11. Splitting strings with split()


name="My name is Akash"
print(name)
print(name.split())


# 12. Converting integer objects to Strings

num=str(input("Enter the no."))
print(num)
print(type(num))


# 13. Converting to uppercase and lowercase

name="My name is Akash"
print(name.lower())
print(name.upper())