## DNA Sequence Processing:

This program analyze.py is designed to process a DNA sequence provided from a FASTA or Genebank file. <br>
It can find the longest repeating subsequence in the full sequence and/or find palindromic subsequences,<br>
based on the user speicifc request. 

## Running the program : 
The program uses command-line arguments allowing the user to provide a file of interest (in FASTA or Genebank text formats) <br>
and one or both  processing option  --longest_rep_seq  --find_palindromes. 

For example: python ./analyze.py  FASTA_text.txt --find_palindromes --longest_rep_seq

## Logic :  

### Input Handling:
The program reads the file, determines its format and parses it to extract the DNA sequence.

### Processing Pipelines:
Based on the selected processing option, the program loads the DNA sequence into the relevant pipeline, <br>
to perform one or both of the following analyses:
- Longest Repeating Subsequence - dentifies the longest subsequence that appears more than once and reports it and it's length.
- Palindromic Subsequences - finds palindromic subsequences (5 nucleotides or longer) and reports their starting positions in the sequence.

