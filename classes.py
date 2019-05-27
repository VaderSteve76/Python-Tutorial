# a class is like a blueprint for creating objects an object has properties and methods
# (functions) associated with it. Almost everything in python is an object


# create a class
class User:
  # constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
    self.age += 1


# extend class
class Customer(User):
# constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance

  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# init user object
john = User('John Doe', 'test@mail.com', 40)

# init customer object
jane = Customer('Jane Doe', 'jdoe1@mail.com', 35)
jane.set_balance(500)

print(type(john))

# property
print(john.name)

# method
john.has_birthday()
print(john.greeting())