# JSON is commonly used with API's, here is how to parse json into a python dictionary


import json

# sample json
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 40}'

# parse to dictionary
user = json.loads(userJSON)

print(user)
print(user['first_name'])

# make dictionary into json
car = {'Make': 'Ford', 'Model': 'Mustang', 'Year': 1964}

carJSON = json.dumps(car)
print(carJSON)