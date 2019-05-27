# a module is basically a file containing a set of functions 
# to include in your application. there a core modules you can install using pip
# including django and other custom modules


# core modules
import datetime
from datetime import date
import time
from time import time

# pip module
from camelcase import CamelCase

# import custom module
import validator
from validator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()
print(c.hump('hello there everyone'))

email = 'testuser@testmail.com'
if validate_email(email):
  print('Email is valid')
else:
  print('Email is bad')

print(timestamp)