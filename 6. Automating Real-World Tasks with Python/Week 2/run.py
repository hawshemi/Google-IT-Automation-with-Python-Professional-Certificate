#!/usr/bin/env python3


import os
import requests


# Define the source directory where feedback files are located
src_dir = "/data/feedback/"

# Get a list of files in the source directory
files = os.listdir(src_dir)

# Function to read lines from a file and return them as a list
def readlines(file):
    with open(src_dir + file) as f:
        lines = f.read().splitlines()
    return lines

# List to store the feedback data
feedback = []

# Keys for the feedback dictionary
keys = ["title", "name", "date", "feedback"]

# Process each file in the source directory
for file in files:
    # Read the lines from the file
    lines = readlines(file)
    # Create a dictionary for the feedback entry and append it to the list
    feedback.append(dict(zip(keys, lines)))

# URL for sending the feedback data
url = "http://localhost/feedback/"

# Send each feedback entry to the server
for entry in feedback:
    # Send a POST request to the server with the feedback data
    response = requests.post(url, data=entry)
    # Check if the response from the server is successful (status code 200-299)
    if response.ok:
        print("loaded entry")
    else:
        # If there was an error with the server response, print the status code
        print(f"load entry error: {response.status_code}")
