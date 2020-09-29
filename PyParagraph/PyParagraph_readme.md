## PyParagraph

![Language](/PyParagraph/Images/language.png)

### Instructions
In this challenge, you get to play the role of chief linguist at a local learning academy. As chief linguist, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.

Your task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:

* Import a text file filled with a paragraph of your choosing.

* Assess the passage for each of the following:

  * Approximate word count

  * Approximate sentence count

  * Approximate letter count (per word)

  * Average sentence length (in words)

* As an example, this passage:

> “Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold.”

...would yield these results:

```output
Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.6
Average Sentence Length: 24.0
```

### Resources
Two files were provided named paragraph_1.txt and paragraph_2.txt in the raw_data directory.    Additionally in the homework verbiage, a third paragraph was provided with the expected output.   I put this additional paragraph in the same directory using a name of paragraph_3.txt.

#### paragraph_1.txt
```
Gene expression in mammals is regulated by noncoding elements that can affect physiology and disease, yet the functions and target genes of most noncoding elements remain unknown. We present a high-throughput approach that uses clustered regularly interspaced short palindromic repeats (CRISPR) interference (CRISPRi) to discover regulatory elements and identify their target genes. We assess >1 megabase of sequence in the vicinity of two essential transcription factors, MYC and GATA1, and identify nine distal enhancers that control gene expression and cellular proliferation. Quantitative features of chromatin state and chromosome conformation distinguish the seven enhancers that regulate MYC from other elements that do not, suggesting a strategy for predicting enhancer–promoter connectivity. This CRISPRi-based approach can be applied to dissect transcriptional networks and interpret the contributions of noncoding genetic variation to human disease.
```
#### paragraph_2.txt
```
When Jackie Chan saw an Oscar at Sylvester Stallone's house 23 years ago, he said that was the moment he decided he wanted one.

On Saturday at the annual Governors Awards, the Chinese actor and martial arts star finally received his little gold statuette, an honorary Oscar for his decades of work in film.

"After 56 years in the film industry, making more than 200 films, after so many bones, finally," Chan, 62, quipped at the star-studded gala dinner while holding his Oscar.

The actor recalled watching the ceremony with his parents and his father always asking him why he didn't have Hollywood's top accolade despite having made so many movies.

He praised his hometown Hong Kong for making him "proud to be Chinese," and thanked his fans, saying they were the reason "I continue to make movies, jumping through windows, kicking and punching, breaking my bones."

The actor was introduced by his "Rush Hour" co-star Chris Tucker, actress Michelle Yeoh and Tom Hanks, who referred to him as "Jackie 'Chantastic' Chan."

Hanks said it was especially gratifying to be able to acknowledge Chan's work because martial arts and action comedy films were two genres often overlooked during awards season.

The Academy of Motion Pictures Arts and Sciences, hosts of the annual ceremony, also bestowed honorary Oscars on British film editor Anne V. Coates, casting director Lynn Stalmaster and prolific documentarian Frederick Wiseman.

The evening was attended by Hollywood's elite, including Denzel Washington, Lupita Nyong'o, Nicole Kidman, Emma Stone, Ryan Reynolds, Amy Adams and Dev Patel.

Stalmaster, 88, credited with securing career-defining roles for actors such as Jeff Bridges, Andy Garcia, Christopher Reeve and John Travolta, is the first casting director to receive an Oscar.
```
#### paragraph_3.txt
```
“Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold.”
```

### Process
The program main.py sets up access to the raw_data directory under PyParagraph and loops all of the files in this directory and performs the analysis for all files in that directory:
* For each file the process reads in the file and opens a file for output that is PyParagraph_Results_ plus the file name being processed.
* The variable list_lines contains the paragraph from the file split into a first try of by sentence.   It was noticed that one of the files has an initial that is causing a sentence to be split in the wrong place.   Upon research, I realized that Mr., Mrs., Miss, Ms. would all cause the same problem.   The split files are looped through to check for this situation.   If the end of a sentence contains one of the above titles than the line is combined with the next line.   And if the sentences ends in a single letter and a period and the prior word is capitalized, then the program assumes we are dealing with an initial and puts the sentence together with the next sentence.
* Once we believe we have a good list of sentences, the process loops through each sentence and splits by word.   Since one of the calculations we are going to do is word length, All occurances of  \n, ., !, ? are replaced with nothing so that the word length does not get artifically increased due to punctutation.
* Additionally, on one of the paragraphs, my program got a different word count than Micrsoft Word did and it was because >1 was being counted as 1 word in my program but 2 in Microsoft Word.   So I also replaced < and > to <space and >space before processing the word sentence.
* The variables line_words_list and line_word_counts were created for for each sentence.  The variable line_words_list contains a list of the words for each sentence and line_word_counts contains a list of word counts for each sentence.
* Additionally variables word_list and word_letter_count are created for each word in all sentences
* Once the loop through the data is complete, the variable output is created with all of the summary information required.
* The final task performed is to output the data in the variable output to the screen and write it to the file /Analysis/PyParagraph_Results_<file name>.txt.


### Output

#### Screen Output
![Screen_Output](/PyParagraph/Analysis/PyParagraph_Results_Screen.jpg)

#### File Output
![File_Output](/PyParagraph/Analysis/PyParagraph_Results_File_1.jpg)
![File_Output](/PyParagraph/Analysis/PyParagraph_Results_File_2.jpg)
![File_Output](/PyParagraph/Analysis/PyParagraph_Results_File_3.jpg)