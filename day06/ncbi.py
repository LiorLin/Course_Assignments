# -*- coding: utf-8 -*-
"""ncbi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ATpZnAGlQSjJcC0KDghYqQFyK7MZGaVa
"""

pip install biopython

from Bio import Entrez
import os
import csv
from datetime import datetime

# This function downloads the indicated number of search results for term.
def ncbi_downloader(term, number):
    Entrez.email = "Lior.lin@weizmann.ac.il"
    search_handle = Entrez.esearch(db='nucleotide', term=term, retmax=number)
    esearch_data = Entrez.read(search_handle)
    total = esearch_data["Count"]
    search_handle.close()
    return esearch_data, total

# For coding and debugging convenience :
esearch_data, total = ncbi_downloader('REST', 10)
print(esearch_data)
print(total)

# This function saves each result item in its own file, and prints the names of the files.

def save_to_files(esearch_data, term):
  id_list = esearch_data['IdList'] # Calling a key in a tuple.
  # print(id_list)

  file_names = []

  for i, id in enumerate(id_list):
    fetch_handle = Entrez.efetch(db='nucleotide', id=id, rettype='FASTA', retmode='text')
    file_data = fetch_handle.read()
    fetch_handle.close

    file_name = f"{term}_{i+1}"
    with open(file_name, "w") as file :
        file.write(file_data)
    file_names.append(file_name)
  return file_names

# For coding and debugging convenience :
save_to_files(esearch_data, 'REST')

def log_file(db, term, num, total):
  log_filename = "ncbi_download_log.csv"
  file_exists = os.path.isfile(log_filename)

  with open(log_filename, "a", newline="") as csvfile:
    fieldnames = ["Date", "Database", "Search Term", "Number Requested", "Total Found"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    if not file_exists:
            writer.writeheader()

    writer.writerow({"Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"Database": db,"Search Term": term,"Number Requested": num, "Total Found": total})

# For coding and debugging convenience :
log_file('nucleotide', 'REST', 10, total)

