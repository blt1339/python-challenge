## PyBank
![Revenue](/PyBank/Images/revenue-per-lead.png)

### Instructions
* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.


### Resources
budget_data.csv is in the Resources directory and is the data that was utilized in the execution of main.py in the PyBank directory.


### Process
The program main.py sets up access to the budget_data.csv file and loops through the file collecting the following inforamtion:
* The number of months is stored in the variable no_months and is increased each loop through the data.
* The total profit and loss accross all of the data is stored in the variable net_pl_amount.
* The previous month and the previous profit and loss amount are stored in variables prev_pl_month and prev_pl_amount (initially set to None).  This allows for a comparision between months except the first loop through the data (when the values are None).
* The greatest increase of profit and loss is stored in the variables increase_pl_month and increase_pl_amount_change with both intially set to None.
* The greatest decrease of profit and loss is stored in the variables decrease_pl_month and increase_pl_amount_change with both intially set to None.
* Once the loop through the data is complete, the variable output is created with all of the summary information required.
* The final task performed is to output the data in the variable output to the screen and write it to the file /Analysis/PyBank_Results.txt.

### Output

#### Screen Output
![Screen_Output](/PyBank/Analysis/PyBank_Results_Screen.jpg)

#### File Output
![File_Output](/PyBank/Analysis/PyBank_Results_File.jpg)