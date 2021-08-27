# Array

# 1. Write a function to add integer values of an array
from array import *
arr=array('i',[])

n=int(input("Enter the Length of the array"))

for i in range(n):
    x =int(input("Enter the Length of the array"))
    arr.append(x)
print(arr)




# 2. Write a function to calculate the average value of an array of integers

orders = [1,2,32,33,46,78,99,99,54]

average = sum(orders) / len(orders)

print("The average coffee order price today is " + str(round(average)))



# 3. Write a program to find the index of an array element

animals = ['cat', 'dog', 'rabbit', 'horse']
index = animals.index('dog')
print(index)

# 4. Write a function to test if array contains a specific value

array = [23,32,2,21,23]
value= 2 in array
print(value)
value = 5 in array
print(value)




# 5. Write a function to remove a specific element from an array

array = [23,32,2,21,23]
print(array)#before remove
array.remove(21)
print(array)# after remove



#6. Write a function to copy an array to another array

array = [23,32,2,21,23,'vikash']

x = array.copy()
x.append(2)
print(x) 
print(array)


# 7. Write a function to insert an element at a specific position in the array

array = [23,32,2,21,23,'vikash']

array.insert(6, "rawat")
print(array)
print(array.index("rawat"))


#8. Write a function to find the minimum and maximum value of an array
array = [1,2,32,45,66,77,88]
print("maximum number of the array is :",max(array))
print("minimum number of the array is :",min(array))


# 9. Write a function to reverse an array of integer values


a=[1,2,32,45,66,77,88]

a.reverse()
print("revers number is :",a)


#10. Write a function to find the duplicate values of an array

arr = [1, 2, 3, 4, 2, 7, 8, 8, 3]
print("Duplicate elements in given array: ")

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i] == arr[j]):
            print(arr[j])


#11. Write a program to find the common values between two arrays

list1 = [1, 2,3,4,5,6]
list2 = [1, 3,4,5]
list1_set = set(list1)
intersection = list1_set. intersection(list2) 
intersection_list = list(intersection)
print("Common numbers of two array is :",intersection_list)


# 12. Write a method to remove duplicate elements from an array

list1 = [1, 2,3,4,5,6,2,1,3]
list2=set(list1)
set1=list(list2)  # Simple way
print(set1)


my_list = [1, 2, 3, 1, 2, 4, 5, 4 ,6, 2]
print("List Before ", my_list)
temp_list = []

for i in my_list:
    if i not in temp_list: 
        temp_list.append(i)

my_list = temp_list

print("List After removing duplicates ", my_list)



# 13. Write a method to find the second largest number in an array


list1 = [10, 20, 4, 45, 99]

mx=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
	if list1[i]>mx:
		secondmax=mx
		mx=list1[i]
	elif list1[i]>secondmax and mx != list1[i]:
		secondmax=list1[i]

print("Second highest number is : ",str(secondmax))


# 14. Write a method to find number of even number and odd numbers in an array

list1 = [1,2,3,4,5,6,7,8,9]
  
even_count=0
odd_count=0

for num in list1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Odd numbers in the list: ", odd_count)         
print("Even numbers in the list: ", even_count)

# 15. Write a function to get the difference of largest and smallest value

arr = [1,2,3,4,5,6,7,8,9,10]
list=max(arr)-min(arr)
print(list)

# 16. Write a method to verify if the array contains two specified elements(12,23)

arr=[1,21,21,12,23,45]
print(arr[3:5])




# 17. Write a program to remove the duplicate elements and return the new array

my_list = [1, 2, 3, 1, 2, 4, 5, 4 ,6, 2]
print("List Before ", my_list)
temp_list = []

for i in my_list:
    if i not in temp_list: 
        temp_list.append(i)

my_list = temp_list

print("New array ", my_list)