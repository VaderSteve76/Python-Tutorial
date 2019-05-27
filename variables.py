# a variable is a container for a value, which can be of various types

'''
this is a
multi line comment
or docstring (used to define a functions purpose)
an be single or double quotes
'''

"""
variable rules:
- Variable names are case sensitive (name and NAME are different variables)
- must start with a letter or an underscore
- can have numbers but not start with one
"""

'''
x = 1            # int
y = 2.5          # float
name = 'Steve'   # str
is_cool = True   # boolean
'''

# multiple assignment
x, y, name, is_cool = (1, 2.5, 'Steve', True)

# basic math
a = x + y

# casting
x = str(x)
y = int(y)
z = float(y)

print(type(x))
print(type(y), y)
print(type(z), z)
print(x, y, name, is_cool, a)