# 1. Truthy/Falsy Real-World Case:
#   Example 1:  User Authentication:


userName = input("Username: ")

if not userName:
    print("Please enter valid username!")

# Example 2: When its an integer but not zero

roll = int(input("Please enter your roll number: "))

if not roll:
    print("please enter a valid roll number")
else: 
    print(f"Your roll number is: {roll}")

# zooming a little,
# if is basically followed by a condition which dictates if the block will be executed! 
# if True: execute
# if False: Don't!

# Okay, so... 
# roll = 0 is Falsy,

# if Falsy will not execute, 
# if not Falsy is truly
# then only it will execute
