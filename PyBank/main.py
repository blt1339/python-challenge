import csv
from os import path


# setup the filepath for the csv file we want to read
filename = "budget_data.csv"
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "Resources", filename))

# Initialize variables
no_months = 0
net_profit_loss = 0
profit_loss = {}

with open(filepath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Go by the header row
    next(csv_reader)
    
    for row in csv_reader:
        no_months += 1

        month = row[0]
        profit_loss_for_month = int(row[1])
        profit_loss[month] = profit_loss_for_month   
            
        net_profit_loss += profit_loss_for_month

    print(no_months)
    print(net_profit_loss)
    print(profit_loss)