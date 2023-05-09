# 1
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [filename.replace('.hpp', '.h') if filename.endswith('.hpp') else filename for filename in filenames]

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# 2
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  pig_latin_words = []

  for word in words:
    # Create the pig latin word and add it to the list
    pig_latin_word = word[1:] + word[0] + "ay"
    pig_latin_words.append(pig_latin_word)
  # Turn the list back into a phrase
  pig_latin_text = " ".join(pig_latin_words)
  return pig_latin_text
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"



# 3
# Which list method can be used to add a new element to a list at a specified index position?
list.insert(index, x)



# 4
# Tuples and lists are very similar types of sequences. What is the main thing that makes a tuple different from a list?
# A tuple is immutable



# 5
def group_list(group, users):
  members = ", ".join(users)
  return "{}: {}".format(group, members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"



# 6
def guest_list(guests):
    for guest in guests:
        name, age, profession = guest
        print("{} is {} years old and works as {}".format(name, age, profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
