# # Oops

# class Person:  # Blueprint Class name should be Capitalize format

#    # __init__ refers to constructor

#    def __init__ (self,name,age,place):  # properties or attributes
      
#       self.name = name  # self refers that it belongs to  current class()

#       self.age = age
      
#       self.place = place

#    def getAge(self):  # methods

#       print(f"i am {self.age} years old")


# p1 = Person('srinivas',1000,'ABC')

# print(p1.name)    # calling attributes

# p1.getAge()  # calling methods


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

# class Atm_pin :

#    def password(self):

#       return 'Your ATM is correct'

# class Upi_pin :

#    def password(self):
      
#       return 'Your UPI pin is correct'

# atm = Atm_pin()

# print(atm.password())

# Upi = Upi_pin()

# print(Upi.password())
