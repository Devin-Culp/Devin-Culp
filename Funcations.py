'''
# import math brings the math module in
import math

# help(math) brings up help page for the math module on run
help(math)

# imports a specific function from math
from math import acos
'''

# def creates a function within the code
# sayHello is the name of the funcation
# (honestly don't know what name does but code won't work without it)
# : searches for the following
# greeting = defines the greeting variable
# ('Hello ' + name) concatonizes the string 'Hello' and the name variable
# return greeting makes the code save the function and wait for use... I think
def sayHello(name):
    greeting = ('Hello ' + name)
    return greeting

# defines user
person = input("What is your name? ")

# defines greeting as the above function + the input name
greeting = sayHello(person)

# prints the final result
print(greeting)
