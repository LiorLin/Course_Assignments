# Function to read a FASTA/Genebank sequence :

import re
from Bio import SeqIO

def read_seq(file_path):
  try:
    with open(file_path, "r") as file:
      first_line = file.readline().strip()

      # Detect format based on the content
      if first_line.startswith(">"):  # FASTA format
        format_type = "fasta"
      elif first_line.startswith("LOCUS"):  # GenBank format
        format_type = "genbank"
      else:
        raise ValueError("Unsupported file format. Please provide a FASTA or GenBank file.")

      # Use the detected format to parse the file
      with open(file_path, "r") as file:
        record = SeqIO.read(file, format=format_type)
        DNA_seq = str(record.seq)  # Extract sequence as a string
        return DNA_seq

  except Exception as e: # Catches exceptions that occur during the file processing.
      print(f"Error reading the file: {e}") # prints a descriptive error message for the user.
      return None # Returns non if an error occurs

def longest_rep_seq(sequence):
  
# Start with the maximum possible length (half sequence) and decrease by one, until a minimum of two letters. 
# For each length, create sequentially all the subsequences of that length,starting from the first letter of
# the sequence, until the end of the sequence such that the last letter is included, but no subsequence
# exceeds the full sequence. Than use regular expressions to search for that subsequence in the full sequence. 

  seq_len = len(sequence)

  if seq_len % 2 != 0 : # if the sequence length is odd, substract one to make even. 
    seq_len -= 1 

  for subseq_len in range(seq_len // 2, 1, -1):  
    for i in range(seq_len - subseq_len + 1):
      subseq = sequence[i : i + subseq_len]

      matches = re.findall(f"(?={re.escape(subseq)})", sequence)
      if len(matches) > 1:
        return subseq

  return None

def find_palindromes(sequence, min_length = 5): # five is the default minimal length

# Iterate over all possible substring lengths that is between 5 letters to the full length
# of the sequence. For each length, create sequentially all the subsequences of that length
# starting from the first letter of the sequence, until the end of the sequence such that the
# last letter is included, but no subsequence exceeds the full sequence. For each substring 
# check if it reads the same forward and backwards.

  seq_len = len(sequence)
  palindromes = [] 

  for length in range(min_length, seq_len + 1):
        for i in range(seq_len - length + 1):
            subseq = sequence[i:i + length]  # Extract substring
            if subseq == subseq[::-1]:  # Check if it reads the same backward
                palindromes.append((subseq, i))

  return palindromes


