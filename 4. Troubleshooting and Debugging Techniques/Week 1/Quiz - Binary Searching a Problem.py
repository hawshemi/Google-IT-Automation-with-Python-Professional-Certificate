# Q 1
# Run the script with the first half of the computers.



# ==========================================================================
# Q 2
def find_item(lst, item):
    # Returns True if the item is in the list, False if not.
    for i in lst:
        if i == item:
            return True
    return False

# Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex"))  # True
print(find_item(list_of_names, "Andrew"))  # False
print(find_item(list_of_names, "Drew"))  # True
print(find_item(list_of_names, "Jared"))  # False



# ==========================================================================
# Q 3
def binary_search(list, key):
    # Returns the position of key in the list if found, -1 otherwise.

    # List must be sorted:
    list.sort()
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle

        if list[middle] > key:
            print("Checking the left side")
            right = middle - 1

        if list[middle] < key:
            print("Checking the right side")
            left = middle + 1

    return -1


print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1))
"""Should print 2 debug lines and the return value:
Checking the left side
Checking the left side
0
"""

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
"""Should print no debug lines, as it's located immediately:
4
"""

print(binary_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
"""Should print 3 debug lines and the return value:
Checking the right side
Checking the left side
Checking the right side
6
"""

print(binary_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
"""Should print 3 debug lines and the return value:
Checking the right side
Checking the right side
Checking the right side
9
"""

print(binary_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
"""Should print 4 debug lines and the "not found" value of -1:
Checking the right side
Checking the right side
Checking the right side
Checking the right side
-1
"""



# ==========================================================================
# Q 4
# head



# ==========================================================================
# Q 5
def linear_search(list, key):
    # Returns the number of steps to determine if key is in the list 

    # Initialize the counter of steps
    steps = 0
    for i, item in enumerate(list):
        steps += 1
        if item == key:
            break
    return steps

def binary_search(list, key):
    # Returns the number of steps to determine if key is in the list 

    # List must be sorted:
    list.sort()

    # The Sort was 1 step, so initialize the counter of steps to 1
    steps = 1

    left = 0
    right = len(list) - 1
    while left <= right:
        steps += 1
        middle = (left + right) // 2
        
        if list[middle] == key:
            break
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return steps

def best_search(list, key):
    steps_linear = linear_search(list, key)
    steps_binary = binary_search(list, key)
    results = "Linear: " + str(steps_linear) + " steps, "
    results += "Binary: " + str(steps_binary) + " steps. "
    if steps_linear < steps_binary:
        results += "Best Search is Linear."
    elif steps_linear > steps_binary:
        results += "Best Search is Binary."
    else:
        results += "Result is a Tie."

    return results

print(best_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
#Should be: Linear: 1 steps, Binary: 4 steps. Best Search is Linear.

print(best_search([10, 2, 9, 1, 7, 5, 3, 4, 6, 8], 1))
#Should be: Linear: 4 steps, Binary: 4 steps. Result is a Tie.

print(best_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
#Should be: Linear: 4 steps, Binary: 5 steps. Best Search is Linear.

print(best_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
#Should be: Linear: 6 steps, Binary: 5 steps. Best Search is Binary.

print(best_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
#Should be: Linear: 10 steps, Binary: 5 steps. Best Search is Binary.