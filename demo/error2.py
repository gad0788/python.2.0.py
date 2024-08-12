# write a script that will take two numbers and display the sum of those numbers

try:
    num1=int(input("please enter the first number: "))
    num2=int(input("please enter the first number: "))
    sum= num1+num2
    print(sum)
except Exception as e:    # this will handle any error when user enters something wrong data.code will not break
    print(" please enter a valid number ")
