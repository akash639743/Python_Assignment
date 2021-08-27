# Static


#1. Define a static variable and access that through a class 

class Car:
       num = 7  
       msg = 'This is a good Car.'  
 
obj = Car()   
print ("Lucky No.", Car.num)  
print (Car.msg)  


#2. Define a static variable and access that through a instance

class Mobile:
    def __init__(self):
        self.model = "Nokia 1200"

    def show_model(self):
        print(self.model)

nokia = Mobile()
print(nokia.model)


# 3. Define a static variable and change within the instance

class Mobile:
    def __init__(self):
        self.model = "Nokia 1200"

    def show_model(self):
        print(self.model)

nokia = Mobile()
print(nokia.model)
nokia.model="Mi 5"
print(nokia.model)



#4. Define a static variable and change within the class

class Mobile:
    @staticmethod
    def show_model(m,p):
        model=m
        price=p
        print(model,price)
realme= Mobile()
Mobile.show_model("Mi 5", 8000)

Mobile.show_model("Nokia", 9000)


