# 1
# What is recursion used for?
# Recursion is used to call a function from inside the same function.


# 2
# Which of these activities are good use cases for recursive programs? Check all that apply.
# Going through a file system collecting information related to directories and files.
# Managing permissions assigned to groups inside a company, when each group can contain both subgroups and users.


# 3
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1

  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False


# 4
# I dunno! Couldn't solve it!


# 5
def sum_positive_numbers(n):
    if n <= 1:
        return n
    return n + sum_positive_numbers(n-1)


print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

