# a tuple is a collection which is ordered and unchangeable. allows duplicate members

# cretae a tuple
fruits = ('apples', 'oranges', 'bananas', 'grapes')

# constructor
# fruits2 = tuple(('apples', 'oranges', 'bananas', 'grapes'))

# single value needs trailing comma to be seen as tuple not str
fruits2 = ('apple',)
print(fruits, fruits2)
print(fruits2, type(fruits2))

# get a value from postiton
print(fruits[1])

# can't change tuple values
# fruits[0] = 'pears'

# delete tuple
del fruits2
# print(fruits2)

# get length
print(len(fruits))



# a set is a collection which is unordered an unindexed. No duplicate members