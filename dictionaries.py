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
