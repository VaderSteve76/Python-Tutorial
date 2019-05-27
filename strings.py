# strings in python are surrounded by either single or double quotes

name = 'Steve'
age = 42

# concatenate
print('Hello my name is ' + name + ' and I am ' + str(age))

# string formatting


# arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-strings (3.6+)
print(f'My name is {name} and I am {age}')


# string methods
s = 'hello world'

# capitalize string
print(s.capitalize())

# make all uppercase
print(s.upper())

# make all lower
print(s.lower())

# swap case
print(s.swapcase())

# get length
print(len(s))

# replace
print(s.replace('world', 'everyone'))

# count
sub = 'h'
print(s.count(sub))

# starts with
print(s.startswith('hello'))

# ends with
print(s.endswith('d'))

# split into a list
print(s.split())

# find position
print(s.find('r'))

# is all alphanumeric
print(s.isalnum())

# is all alphatic
print(s.isalpha())

# is all numeric
print(s.isnumeric())

