# a function is a block of code whih only runs when it is called. in python we don't use
# curly brackets we use indentation with tabs and spaces


# create a function
def sayHello(name):
  print(f'Hello {name}')

sayHello('John Doe')

# return values
def getSum(num1, num2):
  total = num1 + num2
  return total

# print(getSum(5, 5))
num = getSum(5, 5)
print(num)



# a lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can have only one expression
# similar to arrow functions in js