# define the variable 'x' as a string
x = "There are %d types of people." % 10
# define the variable 'binary' as a string
binary = "binary"
# define the variable 'do_not' as a string
do_not = "don't"
# define the variable 'y' as a string
y = "Those who know %s and those who %s." % (binary, do_not) #string in string 1

# print the variable 'x'
print x
# print the variable 'y'
print y

# print 'I said' and then the variable 'x'
print "I said: %r." % x #string in string 2
# print 'I also said' and then the variable 'y'
print "I also said: '%s'." % y #string in string 3

# define the variable 'hilarious' as the boolean value false
hilarious = False
# define the variable 'joke_evaluation' as a string
joke_evaluation = "Isn't that joke so funny?! %r" 

# print the string defined as 'joke_evaluation' with the value of the variable 'hilarious' as the formatted character
print joke_evaluation % hilarious

# define the variable 'w' as a string
w = "This is the left side of..."
# define the variable 'e' as a string
e = "a string with a right side."

# print the variables 'w' and 'e' on the same line
print w + e