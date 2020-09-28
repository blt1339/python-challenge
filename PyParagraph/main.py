import os
import re
from statistics import mean

# Get the base path
base_path = os.path.dirname(__file__)

resources_path = os.path.abspath(os.path.join(base_path, "raw_data"))
text_file_list = os.listdir(resources_path)

for text_file_name in text_file_list:
    # Setup the filepath for the text file we want to read
    text_file_path = os.path.abspath(os.path.join(base_path, "raw_data", text_file_name))

    # Setup the filepath for the results file we want to read
    results_file_name = "PyParagraph_Results_" + text_file_name
    results_file_path = os.path.abspath(os.path.join(base_path,"Analysis",results_file_name))

    # Open the text file
    with open(text_file_path, 'r') as text_file:
        lines = text_file.read()
        
        lines = lines.replace('."','. "')
        lines = lines.replace(".\n",". ")


        #temp_word_list = re.split(" ",lines)
        
        #lines_list = re.split('[^\.\!\?]*[\.\!\?])', lines)  
        #lines_list = re.split('[.!?][\s]{1,2}(?=[A-Z])', lines)  
        #lines_list = re.split('[.!?][\s]{1,2}(?=[A-Z])', lines)  
        lines_list = re.split("(?<=[.!?]) +", lines)


        no_lines = len(lines_list)
        cntr = 0
        cleaned_lines_list = []
        
        while cntr <= no_lines-1:
            line = lines_list[cntr]
            line_words = re.split(" ",line)

            if cntr != no_lines:
                if len(line_words[-1]) == 2:
                    if line_words[-2][0].isupper():
                        cntr = cntr + 1
                        line = lines_list[cntr-1] + " " + lines_list[cntr]
            
            cleaned_lines_list.append(line)
            cntr += 1

    line_words_list = []
    line_words_count = []
    word_list = []
    word_letter_count= []

    for line in cleaned_lines_list:
        line = line.replace("\n","")
        line = line.replace(".","")
        line = line.replace("!","")
        line = line.replace("!","")
        #line = line.replace("'","")      
        line = line.replace('"',"")      

        line_words = re.split(" ",line)     
        line_words_list.append(line_words) 
        line_words_count.append(len(line_words))

        for word in line_words:
            word_list.append(word)
            word_letter_count.append(len(word)) 

    output = []
    output.append("Paragraph Analysis")
    output.append("-----------------")
    output.append("Approxiamte Word Count: {}".format(len(word_list)))
    output.append("Approximate Sentence Count: {}".format(len(cleaned_lines_list)))
    output.append("Average Letter Count: {}".format(round(mean(word_letter_count),1)))
    output.append("Average Sentence Length: {:.1f}".format(round(mean(line_words_count),1)))
    

    # An finally write out results to a file
    with open(results_file_path, 'w') as results_file:
        print('\n')
        print('\n')
        print('--------------------')
        print(text_file_name)
        print('--------------------\n')

        for output_line in output:
            print(output_line)
            results_file.write(output_line + "\n")


      



