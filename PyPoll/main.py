import csv
from statistics import mean
from os import path
import pprint

# Get the base path
base_path = path.dirname(__file__)

# setup the filepath for the csv file we want to read
csv_file_name = "election_data.csv"
csv_file_path = path.abspath(path.join(base_path, "Resources", csv_file_name))

# Setup the filepath for the results file we want to read
results_file_name = "PyBank_Results.txt"
results_file_path = path.abspath(path.join(base_path,"Analysis",results_file_name))

# Initialize loop variables
total_number_votes = 0
votes_by_candidate = {}
winning_candidate = None
winning_votes = None

# Open the csv file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Go by the header row
    next(csv_reader)

    # Loop through the rows of data
    for row in csv_reader:
        # Grab the candidate the vote is for
        row_candidate = row[2]

        # Add this vote into the total number of votes
        total_number_votes += 1

        # Add this vote into the correct candidates vote tally
        if row_candidate in votes_by_candidate:
            votes_by_candidate[row_candidate] += 1
        else:
            votes_by_candidate[row_candidate] = 1

        # Update the candidate with the most votes
        if winning_candidate == None:
            winning_candidate = row_candidate
            winning_votes = votes_by_candidate[row_candidate]
        else:
            if winning_votes > votes_by_candidate[row_candidate]:
                winning_candidate = row_candidate
                winning_votes = votes_by_candidate[row_candidate]

# Update output with the calculated vote information
output = []
output.append('Election Results')
output.append('-------------------------')
output.append('Total Votes: {}'.format(total_number_votes))
output.append('-------------------------')

# Loop through the array of votes by candidate and add to output
for key, key_votes in votes_by_candidate.items():
    output.append('{}: {:.3f}% ({})'.format(key,round((key_votes/total_number_votes * 100),3),key_votes))

# Add the winning Candidate to the output    
output.append('-------------------------')
output.append('Winner: {}'.format(winning_candidate))
output.append('-------------------------')

# And finally output the information to the screen and the results file
with open(results_file_path, 'w') as results_file:
    for output_line in output:
        print(output_line)
        results_file.write(output_line + "\n")