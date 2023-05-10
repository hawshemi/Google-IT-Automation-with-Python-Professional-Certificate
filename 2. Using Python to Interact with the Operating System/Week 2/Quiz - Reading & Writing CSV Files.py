# 1
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string


# Call the function
print(contents_of_file("flowers.csv"))



# 2
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, newline='') as file:
    # Read the rows of the file
    rows = csv.reader(file)
    # Skip the header row
    next(rows)
    # Process each row
    for row in rows:
      # Format the return string for data rows only
      return_string += "a {} {} is {}\n".format(row[1], row[0], row[2])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))



# 3
# In order to use the writerows() function of DictWriter() to write a list of dictionaries to each line of a CSV file, what steps should we take? (Check all that apply)

# Create an instance of the DictWriter() class
# Write the fieldnames parameter into the first row using writeheader()
# Open the csv file using with open



# 4
# Which of the following is true about unpacking values into variables when reading rows of a CSV file? (Check all that apply)

# We need the same amount of variables as there are columns of data in the CSV 
# Rows can be read using both csv.reader and csv.DictReader
# An instance of the reader class must be created first



# 5
# If we are analyzing a file's contents to correctly structure its data, what action are we performing on the file?

# Parsing

