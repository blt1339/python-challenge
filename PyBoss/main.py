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

# Setup a dictionary to translate to 2 character states
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
# Initialize list to store converted data
output_data = []

# Add a row of headings for the first row of our list to store converted data
output_data.append(["Emp ID","First Name","Last Name","DOB","SSN","State"])


# Open the csv file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Go by the header row
    headers = next(csv_reader)

    # Loop through the rows of data
    for row in csv_reader:
        emp_id = row[0]
        name = row[1]
        first_name, last_name = name.split()
        dob = row[2]
        output_dob = datetime.datetime.strptime(dob, "%Y-%m-%d").strftime("%m/%d/%Y")
        ssn = row[3]
        output_ssn = "***-**-" + ssn.split('-')[2]
        state = row[4]
        state_abbrev = us_state_abbrev[state]

        # Add converted data to output_data
        output_data.append([emp_id,first_name,last_name,output_dob,output_ssn,state_abbrev])

    print(output_data)