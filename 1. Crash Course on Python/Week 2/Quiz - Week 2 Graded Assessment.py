# Question 1
# Complete the code to output the statement, “Diego’s favorite food is lasagna”.
# Remember that precise syntax must be used to receive credit.

name = "Diego"
fav_food = "lasagna"
print(name + "’s favorite food is " + fav_food) 



# Question 2
# What is the value of this Python expression: "blue" == "Blue"?

# False


# Question 3
# In the following code, what would be the output?

number = 4
if number * 4 < 15:
 print(number / 4)
elif number < 5:
 print(number + 3)
else:
 print(number * 2 % 5)

# Answer: 7


# Question 4
# Consider the following scenario about using if-elif-else statements:
# The fall weather is unpredictable.  If the temperature is below 32 degrees Fahrenheit, a heavy coat should be worn.
# If it is above 32 degrees but not above 50 degrees, then a jacket should be sufficient.
# If it is above 50 but not above 65 degrees, a sweatshirt is appropriate, and above 65 degrees a t-shirt can be worn.  
# Fill in the blanks in the function below so it returns the proper clothing type for the temperature.

def clothing_type(temp):
    if temp > 65:
        clothing = "T-Shirt"
    elif temp > 50:
        clothing = "Sweatshirt"
    elif temp > 32:
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing


print(clothing_type(72)) # Should print T-Shirt
print(clothing_type(55)) # Should print Sweatshirt
print(clothing_type(65)) # Should print Sweatshirt
print(clothing_type(50)) # Should print Jacket
print(clothing_type(45)) # Should print Jacket
print(clothing_type(32)) # Should print Heavy Coat
print(clothing_type(0)) # Should print Heavy Coat


# Question 5 
# When using an if statement, the code inside the if block will only execute if the conditional statement returns what?

# True


# Question 6 
# Fill in the blanks to complete the function.
# The character translator function receives a single lowercase letter, then prints the numeric location of the letter in the English alphabet.
# For example, “a” would return 1 and “b” would return 2.
# Currently, this function only supports the letters “a”, “b”, “c”, and “d” It returns "unknown" for all other letters or if the letter is uppercase.

def letter_translator(letter):
    if letter == "a":
        letter_position = 1
    elif letter == "b":
        letter_position = 2
    elif letter == "c":
        letter_position = 3
    elif letter == "d":
        letter_position = 4
    else:
        letter_position = "unknown"
    return letter_position


print(letter_translator("a")) # Should print 1
print(letter_translator("b")) # Should print 2
print(letter_translator("c")) # Should print 3
print(letter_translator("d")) # Should print 4
print(letter_translator("e")) # Should print unknown
print(letter_translator("A")) # Should print unknown
print(letter_translator("")) # Should print unknown


# Question 7 
# Can you calculate the output of this code?

def difference(x, y):
    z = x - y
    return z


print(difference(5, 3))

# Answer: 2

# Question 8
#What's the value of this Python expression?

x = 5*2
((10 != x) or (10 > x))

# Answer: False


# Question 9
# Fill in the blanks to complete the function. The “make_positive” function takes in a number and converts that number to its positive equivalent.
# Complete the function to accomplish the following tasks:
# use an if statement to test if the number is negative;
# use a calculation inside the if statement to change the negative number to be positive;
# use a calculation in the else statement to return any positive “number” unchanged.

def make_positive(number):
    if number < 0:
        result = number * -1 
    else:
        result = number
    return result


print(make_positive(-4))   # Should print 4
print(make_positive(0))    # Should print 0
print(make_positive(-.25)) # Should print 0.25
print(make_positive(5))    # Should print 5


# Question 10
# What are some of the benefits of good code style? Select all that apply.

# Easier to maintain
# Makes the intent of the code obvious