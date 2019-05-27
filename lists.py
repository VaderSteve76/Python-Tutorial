# a list is a collection which is ordered and changeable. allows duplicate members



# create list
numbers = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'bananas', 'grapes']

# use a constructor
numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)

# get a single value from a list
print(fruits[1])

# change a value
fruits[0] = 'blueberry'
print(fruits)
fruits[0] = 'apples'
print(fruits)

# get length
print(len(fruits))

# append to list
fruits.append('mangos')
print(fruits)

# remove from list
fruits.remove('grapes')
print(fruits)

# insert to specific position
fruits.insert(2, 'strawberry')
print(fruits)

# remove with pop
fruits.pop(2)
print(fruits)

# reverse list
fruits.reverse()
print(fruits)

# sort list
fruits.sort()
print(fruits)

# reverse sort
fruits.sort(reverse=True)
print(fruits)
