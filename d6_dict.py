# Create dictionary users with:
# Keys: usernames
# Values: tuples with (age, email)

userDetails = {'Harshdeep' : (22, 'myemail@gmail.com'), 'Nicolas' : (29, 'myfemale@gmail.com')}

# Add function to find users by email

def searchUser( user: str):
    try:
        email = userDetails.get(user)[1]
        print(email)
    except TypeError:
        print('No User Found!')

userRequested = input('Please type in the username: ').strip().capitalize()
searchUser(userRequested)