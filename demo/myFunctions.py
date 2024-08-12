# In Python, a function is a block of organized, reusable code that is used to perform a specific task.
import os # global variable 
def hello():
    print("Hello Dianna") # anything indempted will run in this function

def hello1(name): # function with one parameter
    print(f"hello {name}")
#hello1('Douce')

def addition(x,y):
    print(x+y) # print to the console only, use return to spill out there ==use return to store in variable
s=addition(2,5)
#print(s)
def addition2(x,y):
    return x+y  # return can store variables and used later
s1= addition2(5,3)
#print(s1)

def Commands(cmd):
    #import os    # local function-variable decralation
    os.system(cmd)
#Commands('pwd')

def ClrearScreen():
    #import os
    os.system('clear')
#ClrearScreen()

    