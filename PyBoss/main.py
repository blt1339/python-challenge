import csv
from os import path
import datetime

# Get the base path
base_path = path.dirname(__file__)

# Setup the filepath for the csv file we want to read
csv_file_name = "employee_data.csv"
csv_file_path = path.abspath(path.join(base_path, "Resources", csv_file_name))

# Setup the filepath for the results file we want to read
results_file_name = "PyBoss_Export.csv"
results_file_path = path.abspath(path.join(base_path,"Analysis",results_file_name))

# Initialize variables
no_months = 0
net_pl_amount = 0

# Open the csv file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Go by the header row
    next(csv_reader)

    # Loop through the rows of data
    for row in csv_reader:
        print(row)

