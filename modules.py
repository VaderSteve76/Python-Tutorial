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

# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()
print(c.hump('hello there everyone'))

print(timestamp)