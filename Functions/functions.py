#creating function
def my_function():
    print("Hello Python")

#calling a function
my_function()


#argument in a function
def student(fname, lname):
    print("The fname of student is {} and lname is {}".format(fname, lname))
student("rohit", "sajjan")


#positional argument
def student(name):
    print("The name of the student is {}".format(name))
student("Gopal")

#using key=value syntax in keyword argument
def family(child3, child2, child1):
    print("The youngest child in family is {}".format(child3))
family(child1="dora", child2="natasa", child3="sophia")


# *args
def family(*kids):
    print("The youngest child in the family is " + kids[2])

family("max", "alex", "finch")


# **kwargs
def family(**kid):
    print("The last name of the kid is {} ".format(kid["lname"]))
family(fname="alex", lname="abram")


#return values
def function(x):
    return 3 * x
print(function(2))
print(function(6))
print(function(4))