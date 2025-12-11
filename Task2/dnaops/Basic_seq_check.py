#This module contains the following functions.
"""
1. Return the length of the DNA sequence.
2. Count each nucleotide (A, T, G, C) separately.
3. Count ambiguous bases (anything not ATGCN).
4. Validate DNA (valid only if base ∈ A/T/G/C/N) → return True/False.
5. Replace invalid characters with "N".
6. Return number of purines (A + G).
7. Return number of pyrimidines (T + C).

"""
seq = "ATGCTTTAGCGANTTGCAXTGCTNRYGCTA"

def length(seq):
    return len(seq)



#2 #3 can be used for both counting bases and ambiguous bases.
def count_bases(seq):
    no_of_A=0
    no_of_T=0
    no_of_G=0
    no_of_C=0
    no_of_N=0
    invalid_bases = 0
    for base in seq:
        if base == 'A':
            no_of_A+=1
        elif base == 'T':
            no_of_T+=1
        elif base == 'G':
            no_of_G+=1
        elif base == 'C':
            no_of_C+=1
        elif base == 'N':
            no_of_N+=1
        else:
            invalid_bases+=1

    print("The number of A is ", no_of_A)
    print("The number of T is ", no_of_T)
    print("The number of G is ", no_of_G)
    print("The number of C is ", no_of_C)
    print("The number of N is ", no_of_N)
    print("The number of invalid bases is ", invalid_bases)



#4
def validate_DNA(seq):

    for base in seq:
        if base == 'A' or base == 'T' or base == 'G' or base == 'C' or base == 'N':
            valid_DNA = True
        else:
            valid_DNA = False
            break

    return valid_DNA


#5
seq2="AGTCNZYVBBBB"

def replace_ambiguous_bases(seq):
    new_seq = ""
    for base in seq:
        if base == 'A' or base == 'T' or base == 'G' or base == 'C':
            new_seq += base
            continue
        else:
            new_seq += 'N'

    return new_seq


#6
seq2="TTTCCCAGC"
def no_of_purines(seq):
    no_of_purines = 0
    for base in seq:
        if base == "A" or base == "G":
            no_of_purines += 1

    print("The number of purines in the given seq is",no_of_purines)


#7
def no_of_pyrimidines(seq):
    no_of_pyrimidines = 0
    for base in seq:
        if base == "T" or base == "C":
            no_of_pyrimidines += 1

    print("The number of pyrimidines in the given seq is", no_of_pyrimidines)


