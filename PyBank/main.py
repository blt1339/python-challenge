import csv
from statistics import mean
from os import path

# setup the filepath for the csv file we want to read
csv_file_name = "budget_data.csv"
results_file_name = "PyBank_Results.txt"
base_path = path.dirname(__file__)
csv_file_path = path.abspath(path.join(base_path, "Resources", csv_file_name))
resultsfile_path = path.abspath(path.join(base_path,results_file_name))

# Initialize variables
no_months = 0
net_pl_amount = 0

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Go by the header row
    next(csv_reader)

    # Initialize loop variables
    prev_pl_month = None
    prev_pl_amount = None
    increase_pl_month = None
    increase_pl_amount_change = None
    decrease_pl_month = None
    decrease_pl_amount_change = None
    pl_amount_changes = []

    for row in csv_reader:
        no_months += 1

        pl_month = row[0]
        pl_amount = int(row[1])

        net_pl_amount += pl_amount

        if prev_pl_month != None:
            pl_amount_change = pl_amount - prev_pl_amount
            pl_amount_changes.append(pl_amount_change)

            if pl_amount_change > 0:
                if increase_pl_month == None:
                    increase_pl_month = pl_month
                    increase_pl_amount_change = pl_amount_change
                else:
                    if pl_amount_change > increase_pl_amount_change:
                        increase_pl_month = pl_month
                        increase_pl_amount_change = pl_amount_change
            else:
                if decrease_pl_month == None:
                    decrease_pl_month = pl_month
                    decrease_pl_amount_change = pl_amount_change
                else:
                    if pl_amount_change < decrease_pl_amount_change:
                        decrease_pl_month = pl_month
                        decrease_pl_amount_change = pl_amount_change
        
        prev_pl_month = pl_month
        prev_pl_amount = pl_amount

output = []
output.append("Financial Analysis")
output.append('------------------')
output.append("Total Months: {}".format(no_months))
output.append("Total: ${}".format(net_pl_amount))
output.append("Average  Change: ${}".format(round(mean(pl_amount_changes),2)))
output.append("Greatest Increase in Profits: {} (${})".format(increase_pl_month,increase_pl_amount_change))
output.append("Greatest Decrease in Profits: {} (${})".format(decrease_pl_month,decrease_pl_amount_change))



with open(results_file_name, 'w') as results_file:
    for output_line in output:
        print(output_line)
        results_file.write(output_line + "\n")