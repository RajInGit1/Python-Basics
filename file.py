# #open file

# file = open('Example.txt', 'r')

# #read file
# file = open('Example.txt', 'r')

# content = file.read()  # read the entire file content
# print(content)

# file.close()

# reading a file line by line
# file = open('Example.txt', 'r')
# for line in file:
#     print(line)
# file.close()

# file = open('Example.txt', 'r')
# content = file.readlines()  # read all lines into a list
# print(content)
# file.close()


#write to file
# file = open('example2.txt', 'w')  # open file in write mode
# file.write('Hello, this is a test file.\n')  # write to the file
# file.write('This is the second line.\n this is third line')  # write another line

# file.close()  # close the file


# using append methiod to add content to a file
# file = open('example2.txt', 'a')  # open file in append mode
# file.write('This is an appended line.\n')  # append a line to the file
# file.close()

#close file using with statement
# with open('Example.txt', 'r') as file:
#     content = file.read()  # read the entire file content
#     print(content)  # print the content of the file