# 1
# Fill in the blanks to print the numbers 1 through 7.
number = 1  # Initialize the variable
while number <= 7:  # Complete the while loop condition
    print(number, end=" ")
    number += 1  # Increment the variable
# Should print 1 2 3 4 5 6 7 


# 2
# Find and correct the error in the for loop below.  The loop should print every even number from 2 to 12.
for number in range(2, 13, 2):
    print(number)

# Should print:
# 2
# 4
# 6
# 8
# 10
# 12


# 3
# Fill in the blanks to complete the “factorial” function.
# This function will accept an integer variable “n” through the function parameters and produce the factorials of this number (by multiplying this value by every number less than the original number [n*(n-1)], excluding 0).
# To do this, the function should:
# accept an integer variable “n” through the function parameters;
# initialize a variable “result” to the value of the “n” variable;
# iterate over the values of “n” using a while loop until “n” is equal to 0;
# starting at n-1, multiply the result by the current “n” value;
# decrement “n” by -1.
# For example, factorial 3 would return the value of 3*2*1, which would be 6.
def factorial(n):
    result = n
    n -= 1
    while n > 0:
        result *= n
        n -= 1
    return result

print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1


# 4
def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(rows): 
        # Complete the inner loop range to control the number of 
        # asterisks per row
        for y in range(x+1): 
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()

rows_asterisks(5)
# Should print the asterisk rows shown above


# 5
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop:
            return_string += str(start)
            if start > stop:
                return_string += ","
            start -= 1
    else:
        return_string = "Counting up: "
        while start <= stop:
            return_string += str(start)
            if start < stop:
                return_string += ","
            start += 1
    return return_string


print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"



# 6 
def odd_numbers(maximum):
    
    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # odd numbers up to and including the "maximum" value.
    for num in range(1, maximum+1, 2): 

        # Complete the body of the loop by appending the odd number
        # followed by a space to the "return_string" variable.
        return_string += str(num) + " "
          
    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()



print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10)) # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed


# 7 
# The following code raises an error when executed. What's the reason for the error?
def decade_counter():
    while year < 50:
        year += 10
    return year

# Failure to initialize the variable



# 8
# What is the first number that will be printed in the first iteration of this loop? Your answer should be only one number.  
for count in range(1, 6):
    print(count+1)


# 9
# What is the final value of "y" at the end of the following nested loop code? Your answer should be only one number.
for x in range(10):
    for y in range(x):
        print(y)


# 10
# The following code causes an infinite loop. Can you figure out what’s incorrect and how to fix it?

def count_to_ten():
  # Loop through the numbers from first to last 
  x = 1
  while x <= 10:
    print(x)
    x = 1


count_to_ten()
# Should print:
# 1
# 2
# 3 
# 4
# 5
# 6
# 7
# 8 
# 9
# 10

# Variable "x" is assigned the value 1 in every loop