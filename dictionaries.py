# a dictionary is a collection which is unordered, changeable and indexed. No duplicates


# create a dictionary
person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 40
}

# constructor
# person2 = dict(first_name='Jane', last_name='Doe', age=40)

print(person)
print(person, type(person))

# get a value
print(person['first_name'])
print(person.get('last_name'))

# add key/value
person['phone'] = '555-555-5555'
print(person)

# get dict keys
print(person.keys())

# get dict items
print(person.items())

# copy a dictionary
person2 = person.copy()
person2['city'] = 'Chicago'
print(person2)

# remove item
del(person['age'])
person.pop('phone')
print(person)

# clear dictionary
person.clear()
print(person)

# get length
print(len(person2))

# list of dictionaries
people = [
  {'name': 'Martha', 'age': 30},
  {'name': 'Donna', 'age': 60}
]
print(people)
print(people[1]['name'])