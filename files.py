# open a file
myFile = open('myFile.txt', 'w')

# get info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# write to files
myFile.write('I Love Python 3')
myFile.write(' and javascript')
myFile.close()

# append to file
myFile = open('myFile.txt', 'a')
myFile.write(' I also really enjoy React')
myFile.close()

# read from a file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)
