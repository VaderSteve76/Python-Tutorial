# if/else condtionals are used to decide to do 
# something based on something being true or false

x = 10
y = 5

# comparison operators (==, !=, <, >, <=, >=) - used to compare values

# simple if
if x > y:
  print(f'{x} is greater than {y}')

# if/else
if x > y:
  print(f'{x} is greater than {y}')
else: 
  print(f'{y} is greater than {x}')

# else/if = elif
if x > y:
  print(f'{x} is greater than {y}')
elif x == y:
  print(f'{x} is equal to {y}')
else: 
  print(f'{y} is greater than {x}')

# nested if
if x > 2:
  if x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# logical operators ( and, or, not) - used to combine conditional statements

# AND both have to be true
if x > 2 and x <= 10:
  print(f'{x} is greater than 2 and less than or equal to 10')

# OR only one has to be true
if x > 2 or x <= 10:
  print(f'{x} is greater than 2 and less than or equal to 10')

# NOT
if not(x == y):
  print(f'{x} is not equal to {y}')



# membership operators (not, not in) - membership operators are used to tets 
# if a sequence is presented in an object
z = 3
w = 6
numbers = [1, 2, 3, 4, 5]

# IN
if z in numbers:
  print(z in numbers)

# NOT IN
if w not in numbers:
  print(w not in numbers)


# identity operators (is, is not) -  compare the objects, not if they are equal
# but if they are the same objectwith the same memory location