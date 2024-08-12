"""write a script that will ask user to enter yes or no as answer, 
if the user answer is not either yes or no, the script should keep asking for valid entry
if the entry is yes or no, the it should display valid entry
"""

user_answer=""
while True: # this condition is always True or False and run bellow commands
    if user_answer not in ['yes', 'no']:
        user_answer= input("Do you want covid shot? please enter (yes or no):  ").strip().lower()
    else:
        print("valid choice!!!")
        break # stop the while loop if not it will keep asking
        