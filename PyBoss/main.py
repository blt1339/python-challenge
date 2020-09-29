import csv
from os import path
import datetime

# Get the base path
base_path = path.dirname(__file__)
    
# Setup the filepath for the csv file we want to read
csv_file_name = "employee_data.csv"
csv_file_path = path.abspath(path.join(base_path, "Resources", csv_file_name))

# Setup the filepath for the results file we want to read
export_file_name = "PyBoss_Export.csv"
export_file_path = path.abspath(path.join(base_path,"Analysis",export_file_name))

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

def file_read():
    '''
    Read the csv file that is setup in csv_file_path
    '''

    # Open the csv file
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
    
        # Go by the header row
        next(csv_reader)

        # Loop through the rows of data
        for row in csv_reader:
            # Get employee id
            emp_id = row[0]

            # Get name and split into first and last name
            name = row[1]
            first_name, last_name = name.split()

            # Get date of birth and switch format to mm/dd/yyyy
            dob = row[2]
            output_dob = datetime.datetime.strptime(dob, "%Y-%m-%d").strftime("%m/%d/%Y")

            # Get the social security number and * out the first two parts of the number
            ssn = row[3]
            output_ssn = "***-**-" + ssn.split('-')[2]
            # Translate the state from full state name to two character state abbreviations
            state = row[4]
            state_abbrev = us_state_abbrev[state]

            # Add converted data to output_data
            output_data.append([emp_id,first_name,last_name,output_dob,output_ssn,state_abbrev])


def file_write():
    '''
    Write out the converted data to export_file_path
    '''

    # Write out the converted data
    with open(export_file_path, 'w', newline='') as export_file:
        csv_writer = csv.writer(export_file)
        csv_writer.writerows(output_data)

def main():
    '''
    Read the data from employee_data.csv, separate the name into first and last, 
    reformat the date to mm/dd/yyyy, * the numbers in the first 2 parts of the
    social security number, and translate state name to state abbrev before outputting 
    to file PyBoss_Export.csv.
    '''
    
    # Read through the csv data and create output_date with converted data 
    file_read()

    # Write out the converted data
    file_write()

    # Output that we have created the file
    print('--->  The file {} has been created <--'.format(export_file_path))

if __name__ == "__main__":
    main()