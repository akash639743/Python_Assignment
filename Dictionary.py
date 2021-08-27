# Dictionary

#1. Create a Dictionary with at least 5 key value pairs of the Student

students={1:"akash",2:"rohit",3:"simran",4:"mohit",5:"sonam"}

print(students)
# 1.1. Adding the values in dictionary

students[6]="soni"
print(students)

# 1.2. Updating the values in dictionary

students.update({7: "mukesh"})
print(students)


# 1.3. Accessing the value in dictionary
x = students[3]
print(x)

# 1.4. Create a nested loop dictionary

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

# 1.5. Access the values of nested loop dictionary

x=myfamily["child2"]
print(x)


# 1.6. Print the keys present in a particular dictionary

print(students.keys())
print(myfamily.keys())


# 1.7. Delete a value from a dictionary


del myfamily
print(myfamily)
