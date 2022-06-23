#The data we need to retrieve

#1. the total number of votes cast

#2. A complete list of canidates who received votes

#3.. The percentage of votes each canidate won

#4. The total number of votes each canidate

#5. The winner based on the popular vote

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
