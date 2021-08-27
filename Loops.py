# # LOOPS

# # 1. Write a program to print “Bright IT Career” ten times using for loop

for x in range(10):
    print("Bright IT Career")


# # 2. Write a java program to print 1 to 20 numbers using the while loop.
i=1
while(i<=10):
    print(i)
    i+=1


# # 3. Program to equal operator and not equal operators

x=1
y=2
print(x==y)
print(x!=y)


# # 4. Write a program to print the odd and even numbers

x=int(input("Enter the numbers :"))
if (x%2==0):
    print("{} is a even number ".format(x))
else:
    print("{} is a odd number ".format(x))


# 5. Write a program to print largest number among three numbers.

a=int(input("Enter the first numbers :"))
b=int(input("Enter the second numbers :"))
c=int(input("Enter the third numbers :"))

if (a>b) and (a>c):
    print("The largest number is a",a)
elif (c>a)and (c>b):
    print("The largest number is c",c)

    
else:
    print("The largest number is b",b)



# # 6. Write a program to print even number between 10 and 20 using while


x=10

while(x<20):
    print("between 10 and 20 even numbers are :", x)
    x=x+2
    
        
    
# # 7. Write a program to print 1 to 10 using the do-while loop statement

num = 1

while True:
    print(num)
    num += 1
    if num>10:
        break


# 8.Write a program to find Armstrong number or not

n=int(input("Enter the number"))
sum=0
order = len(str(n))
copy_n=n
while(n>0):
    digit=n%10
    sum += digit**order
    n=n//10
if (sum == copy_n):
    print("{} is an armstrong number".format(copy_n))
else:
    print("{} is not armstrong number".format(copy_n))


# 9. Write a program to find the prime or not.

num=int(input("Enter the number"))
for i in range(2,num):
    if num % i == 0:
        print("not prime")
        break
else:
    print("prime")


num = int(input("Enter the number"))
if num > 1:
    for i in range(2, num//2):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# # 10. Write a program to palindrome or not

i = int(input("Enter the number"))
rev=0
x=i
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
if(x==rev):
    print(" Palindrome number")
else:
    print("Not a palindrome number")


# 11. Program to check whether a number is EVEN or ODD using switch
n = int(input("Enter a number: "))
print(n,"is Even.") if (n % 2) == 0 else print(n,"is Odd.")

#12. Print gender (Male/Female) program according to given M/F using switch

choice = input ("Enter your gender : (M/F)")
switcher = {'m': 'Male', 'f' :'Female'}
res=switcher.get(choice, "Invslid Entry")
print("gender : ", res)



