import sys

def open_file(filename):
    with open(filename, "r") as fh:
        seq = fh.read().strip()
    return seq


def count_nucleotides(seq):

    # Convert the sequence to uppercase to ensure case insensitivity
    seq = seq.upper()
    
    # Initialize counters for known leters as a dictionary and for and unknown letters as a variable:
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    unknown_count = 0
    
    # Loop through each character in the sequence
    for char in seq:
        if char in counts:
            counts[char] += 1
        else:
            unknown_count += 1
    return counts,unknown_count,seq
    
def print_results(counts, unknown_count, seq):
    
    total = len(seq)
    print(f"The sequence is {total} nucleotides long.")
    
    for letter, count in (counts.items()):
        percent = (count/total)*100
        print(f"{letter} x{count}, {percent:.2f}") 
        
    unknown_percent = (unknown_count/total)* 100
    print(f"{unknown_count} letters are unknown ({unknown_percent:.2f})%")
    return total # For testing purposes

    
def sequence_stats():
    print(sys.argv)    
    if len(sys.argv) < 2:
        exit(f"You didn't adress a file.py containing a sequence. ")
    
    for index in range(1, len(sys.argv)):
        filename = sys.argv[index]
        seq = open_file(filename)
        counts, unknown_count, seq = count_nucleotides(seq)
        print_results(counts, unknown_count, seq)

if __name__ == "__main__":
    sequence_stats()
     