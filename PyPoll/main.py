# dependencies
import os
import csv

# pypoll file paths
election_data = "PyPoll/Resources/election_data.csv"
file_to_output = "PyPoll/analysis/election_analysis.txt"

# initialize variables
total_votes = 0
candidate_votes = {}
candidates = []

# import csv
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip header row

    for row in csvreader:
        total_votes += 1
        candidate = row[2]  # Assuming Candidate is the third column (index 2)

        # Add candidate to list if not already present
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0

        # Increment candidate's vote count
        candidate_votes[candidate] += 1

# output
output = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

# calculate and append candidate stats to output
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

# find the winner
winner = max(candidate_votes, key=candidate_votes.get)

output += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# print output
print(output)

# export to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)