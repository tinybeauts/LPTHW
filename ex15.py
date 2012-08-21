# takes arguments from the command line when calling the script.
from sys import argv

# unpacking the input arguments into 2 variables, script and filename
script, filename = argv

# defining a variable txt that opens the file named by the variable 'filename'
txt = open(filename)

# print the name of the file being opened
print "Here's your file %r:" % filename
# print the contents of the file opened by 'txt'
print txt.read()

# asks for the filename
print "Type the filename again:"
# defines a variable called 'file_again' as whatever the user puts after the > prompt
file_again = raw_input("> ")

# defines a variable called 'txt_again' that opens the file named by the variable 'file_again
txt_again = open(file_again)

# prints the contents of the file opened by 'txt_again'
print txt_again.read()