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
        lines = lines.replace('\n','')
        lines_list = re.split("(?<=[.!?]) +", lines)
        word_list = re.split(" ",lines)

        word_letter_count = []
        for word in word_list:
            word_letter_count.append(len(word))

        line_word_count = []
        for line in lines_list:
            line_words = re.split(" ",line)
            line_word_count.append(len(line_words))
        
        output = []
        output.append("Paragraph Analysis")
        output.append("-----------------")
        output.append("Approxiamte Word Count: {}".format(len(word_list)))
        output.append("Approximate Sentence Count: {}".format(len(lines_list)))
        output.append("Average Letter Count: {}".format(round(mean(word_letter_count),1)))
        output.append("Average Sentence Length: {}".format(round(mean(line_word_count),1)))
    

    # An finally write out results to a file
    with open(results_file_path, 'w') as results_file:
        print('--------------------')
        print(text_file_name)
        print('--------------------\n')
        for output_line in output:
            print(output_line)
            results_file.write(output_line + "\n")
