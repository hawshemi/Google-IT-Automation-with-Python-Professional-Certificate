# 1
# How are while loops and for loops different in Python?
# While loops iterate while a condition is true, for loops iterate through a sequence of elements.


# 2
# Which option would fix this for loop to print the numbers 12, 18, 24, 30, 36?
for n in range(6,18+1,3):
    print(n*2)


# 3
# Which for loops will print all even numbers from 0 to 18? Select all that apply.

for n in range(19):
    if n % 2 == 0:
        print(n)

for n in range(10):
    print(n+n)


# 4
# Fill in the blanks so that the for loop will print the first 10 cube numbers (x**3) in a range that starts with x=1 and ends with x=10.

for X in range(1,11):
  print(X**3)


# 5
# Write a for loop with a three parameter range() function that prints the multiples of 7 between 0 and 100.
# Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7. 

for i in range(0, 101, 7): 
    if i % 7 == 0:
        print(i)