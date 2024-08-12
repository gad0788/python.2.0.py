"""
write a script that will ask a string and tell if a letter in the string is vowel
or consonant.
"""
my_string=input("please enter a word: ").strip()
num_c=0
num_v=0
for i in my_string:
    if i in 'aeiuo':
        num_v+=1 # will increase by one
        #print(f"{i} is vowel ")
    else:
       # print(f"{i} is consonant ")
        num_c+=1
print(f"number of vowel is: {num_v}")
print(f"number of consonant is: {num_c}")