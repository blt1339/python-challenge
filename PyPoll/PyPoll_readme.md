## PyPoll
![Vote Counting](/PyPoll/Images/Vote_counting.png)

### Instructions
* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

### Resources
election_data.csv is in the Resources directory and is the data that was utilized in the execution of main.py in the PyPoll directory.

### Process
The program main.py sets up access to the election_data.csv file and loops through the file collecting the following inforamtion:
* The total number of votes is stored in the variable total_number_votes and is increased each loop through the data.
* The total votes per candidate is stored in the dictionary votes_by_candidate with a key of the candidates's last name.  Each time a specific candidate is encountered, the vote count for that candidate is increased by 1. 
* The last name of the row of data as we loop through the data is stored in the variable row_candidate.
* In order to keep track of the winner, the variables winning_candidate and winning_votes is utilzed.   Both variables start out as None.
* Once the loop through the data is complete, the variable output is created with all of the summary information required.
* The final task performed is to output the data in the variable output to the screen and write it to the file /Analysis/PyBank_Results.txt.

### Output

#### Screen Output
![Screen_Output](/PyPoll/Analysis/PyPoll_Results_Screen.jpg)

#### File Output
![File_Output](/PyPoll/Analysis/PyPoll_Results_File.jpg)