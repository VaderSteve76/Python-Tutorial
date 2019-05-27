# a for loop is used for iterating over a sequence 
# that is either a list, dictionary, tuple, set, or a string

people = ['John', 'Paul', 'Sara', 'Susan']

# simple for loop
for person in people:
  print(f'Current person: {person}')

# break
for person in people:
  if person == 'Sara':
    break
  print(f'Current person: {person}')

# continue
for person in people:
  if person == 'Sara':
    continue
  print(f'Current person: {person}')

# range
for i in range(len(people)):
  print(people[i])

for i in range(0, 11):
  print(f'Number: {i}')



# while loops execute a set of statements as long as a condition is true

count = 0
while count <= 0:
  print(f'Count: {count}')
  count += 1