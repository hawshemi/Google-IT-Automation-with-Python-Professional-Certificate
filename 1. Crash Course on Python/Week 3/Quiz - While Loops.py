
# 1
# In Python, what do while loops do?  
# while loops tell the computer to repeatedly execute a set of instructions while a condition is true.  

# 2
# Which techniques can prevent an infinite while loop? Select all that apply. 
# Change the value of a variable used in the while condition
# Use the break keyword

# 3
def is_power_of_two(number):
  if number <= 0:
    return False
  while number % 2 == 0:
    number = number / 2
  if number == 1:
    return True
  return False

# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False


# 4
def sum_divisors(number):
    # Initialize the appropriate variables
    divisor = 1
    total = 0

    # Avoid dividing by 0 and negative numbers 
    # in the while loop by exiting the function
    # if "number" is less than one
    if number < 1:
        return 0 

    # Complete the while loop
    while divisor < number:
        if number % divisor == 0:
            total += divisor
        # Increment the correct variable
        divisor += 1

    # Return the correct variable 
    return total


print(sum_divisors(0)) # Should print 0
print(sum_divisors(3)) # Should print 1
# 1
print(sum_divisors(36)) # Should print 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should print 1+2+3+6+17+34+51
# 114


# 5
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier 
        if  result > 25 :
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
    
        # Increment the appropriate variable
        multiplier += 1



multiplication_table(3) 
# Should print: 
# 3x1=3 
# 3x2=6 
# 3x3=9 
# 3x4=12 
# 3x5=15

multiplication_table(5) 
# Should print: 
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25

multiplication_table(8) 
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24
