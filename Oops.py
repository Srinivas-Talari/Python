# class Person:  # class(Blue print for objects )

#     def __init__(self,name):   # init func or Constructor func to define all properties  

#         # it is automatically called after object is created

#         self.name = name  # here name is a property# self represents that it belongs to current class

#     def doCode (self):  # Methods

#         print(f"{self.name} codes very well")


# p1 = Person("Srinivas")  # object

# p1.doCode()  #  method call


# Encapsulation

class User :

    def __init__(self,name,password):

        self.name = name

        self.__password = password
    def getName (self):

        print(f"My name is {self.name}")

    def getPassword(self):

        print(f"My password is {self.__password}")

p1 = User('seenu',1234)

p1.getPassword()
    
        
        