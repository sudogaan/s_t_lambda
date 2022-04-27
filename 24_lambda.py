# lambda expressions: expressions that do not have a specific name

# write function to compute 3x+1

def f(x):
	return 3*x + 1
f(2)

#lambda function:
g = lambda x: 3*x + 1
g(2) 

# lambda expressions with multiple inputs
# combine first name(fn) and last name(ln) into a single full name

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
# we used strip to remove undesired whitespace and title to make sure that only the first letters are capitalized.

full_name("      leonard", "EULER")

# writing lambda expressions
# lambda : "what is my purpose?"
# lambda x: 3*x + 1
# lambda x, y: (x*y)**0.5 #geometric mean
# lambda x, y, z: 3/(1/x + 1/y + 1/z) #harmonic mean
# lambda x1, x2, ..., xn: <expression>

# a function with no name
scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]

# create a function that only extracts the last name and uses that as the sorting value
# help(scifi_authors.sort) # to understand how to use the sort function
# first split the string wherever it has a space, next, access the last piece by index -1, and lastly convert the string to lowercase, this way the sorting is not case-sensitive
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())

# write a function that makes functions
# quadratic functions 
# f(x) = ax^2 + bx + c

def build_quadratic_function(a, b, c):
	"""Returns the function f(x) = ax^2 + bx + c """
	return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(2, 3, -5)
f(0) # output: -5
f(1) # output: 0

build_quadratic_function(3, 0, 1)(2) # this code creates 3x^2 + 1 and passes in the value 2, which give us 13

