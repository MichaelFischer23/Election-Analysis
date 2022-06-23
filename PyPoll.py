
# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter.

total_votes = 0 
#decalre list of canidates

candidates_option = []

#declare empty dictionary

candidates_votes = {}

#Winning Canidataed and Winning count Ticker

winning_candidate = ""

winning_count = 0

winning_percentage= 0
# Open the election results and read the file.

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read the header row.

    headers = next(file_reader)

#print each row in csv file.

    for row in file_reader:

        #2. Add total to vote count
        total_votes += 1

# Print the canidates name 

        candidates_name = row[2]

    # If the candidate does not match any existing candidate...

        if candidates_name not in candidates_option:

            #Add canidates name to list

            candidates_option.append(candidates_name)

            #begin tracking

            candidates_votes[candidates_name] = 0

        #add a vote to candidates count

        candidates_votes[candidates_name] += 1  
        
#Iterate through the list  

    for canidates_name in candidates_votes:

#retrieve vote vount
        votes = candidates_votes[candidates_name]

#Calculate vote percentage
        vote_percentage = (votes / total_votes) * 100
    
    #  print each candidate's name, vote count, and percentage of votes

print(f"{candidates_name}: {vote_percentage:.1f}% ({votes:,})\n")

if (votes > winning_count) and (vote_percentage > winning_percentage):

    winning_count = votes

    winning_percentage = vote_percentage

    winning_candidate = candidates_name

# Print the candidate vote dictionary

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)