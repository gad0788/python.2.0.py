# using written functions
#import myFunctions # load all functions in memory
#myFunctions.hello()
#import myFunctions as m # alias of funtion
#m.hello()
from myFunctions import hello, hello1 # import a single or two functions out of list of functions
hello() # call the name of function only
hello1("Elly")

#import os
#os.system('clear')
from os import system
system('clear')