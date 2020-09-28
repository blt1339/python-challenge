import os
import re
from statistics import mean

# Get the base path
base_path = os.path.dirname(__file__)

# Setup a path to the raw_data and grab a list of files there
resources_path = os.path.abspath(os.path.join(base_path, "raw_data"))
text_file_list = os.listdir(resources_path)

# Loop through files in resources file 
for text_file_name in text_file_list:
    # Setup the filepath for the text file we want to read
    text_file_path = os.path.abspath(os.path.join(base_path, "raw_data", text_file_name))

    # Setup the filepath for the results file we want to write
    results_file_name = "PyParagraph_Results_" + text_file_name
    results_file_path = os.path.abspath(os.path.join(base_path,"Analysis",results_file_name))

    # Open the resource text file
    with open(text_file_path, 'r') as text_file:

        # Load all of the data into lines
        lines = text_file.read()
        
        # Make sure that there is a space after the period
        lines = lines.replace('."','. "')
        lines = lines.replace(".\n",". ")

        # Perform first attempt to split by sentence
        lines_list = re.split("(?<=[.!?]) +", lines)


        no_lines = len(lines_list)
        cntr = 0
        cleaned_lines_list = []
        
        while cntr <= no_lines-1:
            line = lines_list[cntr]
            line_words = re.split(" ",line)

            # Figure out if we have incorrectly split due to an initial or prefix (Mr.,Mrs.,Miss)
            if len(line_words[-1]) == 2:
                if line_words[-2][0].isupper():
                    cntr = cntr + 1
                    line = lines_list[cntr-1] + " " + lines_list[cntr]
            else:
                if line_words[-1] == "Mr." or line_words[-1] == "Ms." or line_words[-1] == "Miss." or line_words[-1] == "Mrs.":
                    cntr = cntr + 1
                    line = lines_list[cntr-1] + " " + lines_list[cntr]                    
            
            # Now store the cleaned line and increase the cntr
            cleaned_lines_list.append(line)
            cntr += 1

    # Initialize the variables needed to store analysis information
    line_words_list = []
    line_words_count = []
    word_list = []
    word_letter_count= []

    # Loop through the cleaned lines and analyze them
    for line in cleaned_lines_list:
        
        # Eliminate punctuation that would increase a word length if left
        line = line.replace("\n","")
        line = line.replace(".","")
        line = line.replace("!","")
        line = line.replace("?","")

        # Make sure there is a space after > and < so that it does not get counted with something else 
        line = line.replace('>','> ')
        line = line.replace('<','< ') 
      
        # Split the lines into words and store the words for each line 
        # and the number of words in each line
        line_words = re.split(" ",line)     
        line_words_list.append(line_words) 
        line_words_count.append(len(line_words))

        # Create a list of all of the words and their letter count
        for word in line_words:
            word_list.append(word)
            word_letter_count.append(len(word)) 
    
    # Now that we have all of our analysis information create output of that information
    output = []
    output.append("Paragraph Analysis")
    output.append("------------------")
    output.append("Approxiamte Word Count: {}".format(len(word_list)))
    output.append("Approximate Sentence Count: {}".format(len(cleaned_lines_list)))
    output.append("Average Letter Count: {}".format(round(mean(word_letter_count),1)))
    output.append("Average Sentence Length: {:.1f}".format(round(mean(line_words_count),1)))
    

    # Finally write out results to the screen and a file
    with open(results_file_path, 'w') as results_file:
        print('\n')
        print('\n')
        print('--------------------')
        print(text_file_name)
        print('--------------------\n')

        for output_line in output:
            print(output_line)
            results_file.write(output_line + "\n")