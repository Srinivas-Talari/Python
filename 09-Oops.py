# Oops

class Employee:
    
    def __init__(self,name,id,salary):  #this belongs to objects
        
        self.name = name
        self.id = id
        self.salary = salary
        
        
    def getEmployeeDetails(self):
    
        print(f"His name is {self.name} and id number is {self.id} and his salary is {self.salary}")
    @staticmethod  # if we dont want to use self keyword for normal methods without using attributes
    def getFinished():
        
        print('The process is completed....')
    
emp1 = Employee('seenu',1161,123456)  # objects
emp2 = Employee('talari',1121,456789)
emp3 = Employee('srinivas',1131,9876543)

emp1.getEmployeeDetails()

emp1.getFinished()

Employee.getEmployeeDetails(emp2)


# # Encapsulation (1.binds attributes and methods 2. It will hide the data)

class Bankaccount:

   def __init__(self,owner,balance = 2300):

      self.owner = owner

      self.__balance = balance # private variable

   def amountDeposit (self,amount) :

      if(amount > 0) :

         self.__balance+=amount

         print(f"Deposited {amount} and total balance is {self.__balance}")
      else:
            print("Deposit amount must be positive.")

customer1 = Bankaccount('abc')

# print(customer1.__balance)  # this cant be accessed

customer1.amountDeposit(20000)


# Polymorphism  (same methods but different behaviours)

class Atm_pin :

   def password(self):

      return 'Your ATM is correct'

class Upi_pin :

   def password(self):
      
      return 'Your UPI pin is correct'

atm = Atm_pin()

print(atm.password())

Upi = Upi_pin()

print(Upi.password())


# inheritance

class Human:
    
    def __init__(self,name,color,sound):
        
        self.name = name
        
        self.color = color
        
        self.sound =  sound
        
    def getDetails(self):
        
        print(f'Name:{self.name}, color : {self.color} , sound: {self.sound}')
    
class Animal(Human):
    
    def __init__(self,name,color,sound,bark):
        
        super().__init__(name,color,sound)
        
        self.bark = bark
            
    def getDetails(self):
        
        print(f'Name:{self.name}, color : {self.color} , sound: {self.sound} and {self.bark}')
        
hum1 = Human('seenu','brown','yaaaaaahhh')

anim1 = Animal('tiger','white&Orange','haaaaaaaaahhhh','ababababa')

# print(anim1.bark)

anim1.getDetails()


# Types 

# 1. Single level Inheritance

class Teacher:

    def __init__(self,name,age,place):

        self.name = name

        self.age = age,

        self.place = place

    def getBio(self):  # Over rides this if any method is declared in child class with same function name

        print(f'Name:{self.name} Age:{self.age} Place:{self.place}')

class Student(Teacher):

    def __init__(self,name,age,place,color):

        super().__init__(name,age,place)

        self.color = color
        
    # def getBio(self):

    #         print(f'Name:{self.name} Age:{self.age} Place:{self.place} and My color is {self.color}')
        
a = Student('seenu',25,'BKS','black')

a.getBio()
        

# 2. Multiple  inheritance

class A :
    
    def greet(self):
        
        print('Good Morning...')
        
    def LastWish(self):
        
        print('Good Afternoon...')
    
class B :
    
    def wish(self):
        
        print('Good evening...')
        
    def LastWish(self):
        
        print('Good night...')

class C (B,A) :  # if there are 2 similar methods in both parent classes then it will over-ride(B) if we pass class names as(A,B) reciprocally...
    
    pass

a = C()

a.LastWish()


# Multilevel Inheritance


class A :
    
        def mrng(self):
    
            print('Good Morning')

class B(A):
    
        def after(self):
        
            print('Good Afternoon')

class C(B):
    
        def __init__(self,name):
        
            self.name = name
    
        def evng(self):
        
             print(f'Good Evening{self.name}')

class D(C):
    
        def __init__(self,name,age):
            
            self.age = age
    
            super().__init__(name)
        
        def night(self):
        
            print(f'Good Night {self.name} and i am {self.age} years old')
        
c = C('srinivas')

d = D('talari' ,1000)

d.night()

c.evng()


# Abstraction

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
class Auto(Vehicle):
    
    def start(self):
        
        print('Auto can start with hand rod')
    
class Bike(Vehicle):
    
    def start(self):
        
        print('Bike can start with self') 


class Car(Vehicle) :
    
    def start(self):
        
        print('Car can start by turning on key')
        
# a = Vehicle()

b = Auto()

c = Bike()

d = Car()

b.start()

c.start()

d.start()










    




    
