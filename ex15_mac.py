from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# Extra Credit 4

# from sys import argv
# 
# script, filename = argv
# 
# txt = open(filename)
# 
# print "Here's your file %r:" % filename
# print txt.read()

# Extra Credit 5

# print "Type the filename again:"
# file_again = raw_input("> ")
# 
# txt_again = open(file_again)
# 
# print txt_again.read()

# A reason to get the file name as input rather than when you call the file
# would be if you have a lot of files you're calling
# Another reason is maybe you're calling multiple files, but the names of
# some of them are contained in other ones. So you might need to open them
# before you can call the next one.

# Extra Credit 8

# from sys import argv
# 
# script, filename = argv
# 
# txt = open(filename)
# 
# print "Here's your file %r:" % filename
# print txt.read()
# 
# txt.close()
# 
# print "Type the filename again:"
# file_again = raw_input("> ")
# 
# txt_again = open(file_again)
# 
# print txt_again.read()
# 
# txt_again.close()