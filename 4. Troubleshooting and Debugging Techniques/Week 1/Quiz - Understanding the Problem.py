# Q 1
# What should happen when you open the app?



# Q 2
# The observer effect.



# Q 3
import re

def compare_strings(string1, string2):
    # Convert both strings to lowercase 
    # and remove leading and trailing blanks
    string1 = string1.lower().strip()
    string2 = string2.lower().strip()

    # Ignore punctuation
    punctuation = r"[\.\?!,;:'-]"
    string1 = re.sub(punctuation, "", string1)
    string2 = re.sub(punctuation, "", string2)

    return string1 == string2

print(compare_strings("Have a Great Day!", "Have a great day?"))  # True
print(compare_strings("It's raining again.", "its raining, again"))  # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three."))  # False
print(compare_strings("They found some body.", "They found somebody."))  # False



# Q 4
# Attempt to trigger the problem again by following the steps of our reproduction case.abs



# Q 5
import datetime
from datetime import date

def add_year(date_obj):
    try:
        new_date_obj = date_obj.replace(year=date_obj.year + 1)
    except ValueError:
        # This gets executed when the above method fails,
        # which means that we're making a Leap Year calculation
        new_date_obj = date_obj.replace(year=date_obj.year + 4)
    return new_date_obj

def next_date(date_string):
    # Convert the argument from string to date object
    date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    next_date_obj = add_year(date_obj)

    # Convert the datetime object to string,
    # in the format of "yyyy-mm-dd"
    next_date_string = next_date_obj.strftime("%Y-%m-%d")
    return next_date_string

today = date.today()  # Get today's date
print(next_date(str(today))) 
# Should return a year from today, unless today is Leap Day

print(next_date("2021-01-01")) # Should return 2022-01-01
print(next_date("2020-02-29")) # Should return 2024-02-29
