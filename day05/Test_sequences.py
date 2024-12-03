# Creating a simple test for the business logic count_nucleotides function in sequences_stats

from Functions_sequence_stats import count_nucleotides

a_seq = 'ACCTGXXCXXGTTACTGGGCXTTGTXX'
b_seq = 'ACCGGGTTTT'

def test_count():
    # Test for a_seq
    count_a, unknown_count_a, _ = count_nucleotides(a_seq)
    print(f"count_a: {count_a}, unknown_count_a: {unknown_count_a}")
    assert count_a == {'A': 2, 'C': 5, 'G': 6, 'T': 7}, "Test failed for counting known letter in seq_a"
    assert unknown_count_a == 7, "Test failed for counting unknown letters in seq_a"

    # Test for b_seq
    count_b, unknown_count_b, _  = count_nucleotides(b_seq)
    print(f"count_b: {count_b}, unknown_count_b: {unknown_count_b}")
    assert count_b == {'A': 1, 'C': 2, 'G': 3, 'T': 4}, "Test failed for counting known letter in seq_b"
    assert unknown_count_b == 0, "Test failed for counting unknown letters in seq_b"

# Run the tests
test_count()
print("All tests passed!")

    
