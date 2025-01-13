# This file is called analyze and it gets one or maximum two inputs from the user. 

import re
import sys

from Bio import SeqIO
from func_day09 import read_seq, longest_rep_seq, find_palindromes
# Ensure correct usage of the program
if len(sys.argv) <3 :
    print("Error: At least a file name and one program option (--longest_rep_seq or --find_palindromes) must be provided.")
    print("Usage: python analyze.py <file_path> --longest_rep_seq --find_palindromes")
    sys.exit(1)  # Exit with an error code

# Parse inputs
script_name = sys.argv[0]  # The name of the script (analyze.py)
file_name = sys.argv[1]    # The required file input
options = sys.argv[2:]     # All options provided after the file

# Validate that at least one program option is provided
if "--longest_rep_seq" not in options and "--find_palindromes" not in options:
    print("Error: You must specify at least one option: --longest_rep_seq or --find_palindromes.")
    sys.exit(1)

# Load DNA sequence
DNA_seq = read_seq(file_name)
if not DNA_seq:
    print("Error: Unable to load DNA sequence from the file.")
    sys.exit(1)

if "--longest_rep_seq" in options:
    print("DNA sequence loaded:", DNA_seq)
    subseq= longest_rep_seq(DNA_seq)

    if subseq:
        subseq_len = len(subseq)
        print(f"Longest repeat :", subseq, f", {subseq_len} nucleotides")
    else: 
        print("No repeated sequence found")

if "--find_palindromes" in options:
    palindromes = find_palindromes(DNA_seq)
    
    if palindromes:
        print("Simple Palindromes found:")
        for palindrome, position in palindromes:
            print(f"Palindrome: {palindrome}, Position: {position}")
    else:
        print(f"No palindromes in the sequence")