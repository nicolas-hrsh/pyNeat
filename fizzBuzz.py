# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print 'Fizz' instead of the number and for the multiples of five print 'Buzz'. 
# For numbers which are multiples of both three and five print 'FizzBuzz'


start_range = int(input("Please enter starting of the range: ")) 
end_range = int(input("Please enter the ending of the range: "))

for x in range(start_range, end_range):
    temp_var = ('Fizz'*(x%3==0) + 'Buzz'*(x%5==0)) or (x)  # '' -> False and !'' -> True for right side of or
    print(temp_var)




# HomeWork: 
# Prints Fizz if prime
# Prints Buzz if palindrome
# Prints FizzBuzz if both
# Uses no if or else, only expressions and functions returning booleans multiplied by strings
