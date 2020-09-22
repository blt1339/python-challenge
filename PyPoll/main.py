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


    print('Election Results')
    print('-------------------------')
    print('Total Votes: {}'.format(total_number_votes))
    print('-------------------------')

    for key, key_votes in votes_by_candidate.items():
        print('{}: {}% ({})'.format(key,round((key_votes/total_number_votes * 100),3),key_votes))
    print('-------------------------')
    print('Winner: {}'.format(candidate_with_most_votes))
    print('-------------------------')
