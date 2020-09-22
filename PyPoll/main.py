import csv
from statistics import mean
from os import path
import pprint

# setup the filepath for the csv file we want to read
csv_file_name = "election_data.csv"
results_file_name = "PyBank_Results.txt"
base_path = path.dirname(__file__)
csv_file_path = path.abspath(path.join(base_path, "Resources", csv_file_name))
results_file_path = path.abspath(path.join(base_path,"Analysis",results_file_name))

# Initialize variables
total_number_votes = 0
votes_by_candidate = {}

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Go by the header row
    next(csv_reader)

    # Initialize loop variables
    candidate_with_most_votes = None
    most_votes = None
    


    for row in csv_reader:
        row_candidate = row[2]

        total_number_votes += 1
        if row_candidate in votes_by_candidate:
            votes_by_candidate[row_candidate] += 1
        else:
            votes_by_candidate[row_candidate] = 1

        if candidate_with_most_votes == None:
            candidate_with_most_votes = row_candidate
            most_votes = votes_by_candidate[row_candidate]
        else:
            if most_votes > votes_by_candidate[row_candidate]:
                candidate_with_most_votes = row_candidate
                most_votes = votes_by_candidate[row_candidate]

    output = []
    output.append('Election Results')
    output.append('-------------------------')
    output.append('Total Votes: {}'.format(total_number_votes))
    output.append('-------------------------')

    for key, key_votes in votes_by_candidate.items():
        output.append('{}: {:.3f}% ({})'.format(key,round((key_votes/total_number_votes * 100),3),key_votes))
    output.append('-------------------------')
    output.append('Winner: {}'.format(candidate_with_most_votes))
    output.append('-------------------------')

    with open(results_file_path, 'w') as results_file:
        for output_line in output:
            print(output_line)
            results_file.write(output_line + "\n")