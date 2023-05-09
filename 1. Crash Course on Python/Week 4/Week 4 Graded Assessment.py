# 1
def first_character(string):
    # Complete the return statement using a string operation.
    return string[0] 


print(first_character("Hello, World")) # Should print H
print(first_character("Python is awesome")) # Should print P
print(first_character("Keep going")) # Should print K



# 2
def highlight_word(sentence, word):
    # Complete the return statement using a string method.
    return sentence.replace(word, word.upper())


print(highlight_word("Have a nice day", "nice"))
# Should print: "Have a NICE day"
print(highlight_word("Shhh, don't be so loud!", "loud"))
# Should print: "Shhh, don't be so LOUD!"
print(highlight_word("Automating with Python is fun", "fun"))
# Should print: "Automating with Python is FUN"


# 3
def combine_lists(list1, list2):
    combined_list = [] # Initialize an empty list variable
    list1.reverse() # Reverse the order of "list1"
    combined_list = list2 + list1 # Combine the two lists 
    return combined_list
  
Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]

print(combine_lists(Jaimes_list, Drews_list))
# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']



# 4
def squares(start, end):
    return [ n * n for n in range(start, end + 1) ] # Create the required list comprehension.


print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



# 5
def car_listing(car_prices):
  result = ""
  # Complete the for loop to iterate through the key and value items 
  # in the dictionary.
  for car, price in car_prices.items():
    result += "A {} costs {} dollars\n".format(car, price) # Use a string method to format the required string. 
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Should print:
# A Kia Soul costs 19000 dollars
# A Lamborghini Diablo costs 55000 dollars
# A Ford Fiesta costs 13000 dollars
# A Toyota Prius costs 24000 dollars



# 6
def setup_guests(guest_list):
    # Initialize a new dictionary
    result = {}
    # Iterate over the elements in the list
    for guest in guest_list:
        # Add each list element to the dictionary as a key with
        # the starting value of 0
        result[guest] = 0
    return result

guests = ["Adam","Camila","David","Jamal","Charley","Titus","Raj","Noemi","Sakira","Chidi"]

print(setup_guests(guests))
# Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}



# 7
def count_numbers(text):
    # Initialize a new dictionary.
    dictionary = {}
    # Complete the for loop to iterate through each "text" character.
    for char in text:
        # Complete the if-statement using a string method to check if the
        # character is a number.
        if char.isdigit():
            # Complete the if-statement using a logical operator to check if 
            # the number is not already in the dictionary.
            if char not in dictionary:
                # Use a dictionary operation to add the number as a key
                # and set the initial count value to zero.
                dictionary[char] = 0
            # Use a dictionary operation to increment the number count value 
            # for the existing key.
            dictionary[char] += 1
    return dictionary

print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}
