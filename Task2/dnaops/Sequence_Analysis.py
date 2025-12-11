"""
1. Calculate GC content (entire sequence).
2. Calculate AT content.
3. Calculate GC content for a user-defined region (start–end).
4. Check whether sequence is a palindrome.
5. Return a nucleotide frequency dictionary.
6. Generate a formatted percentage report of each base

"""

#1

def gc_content(seq):
    count=0
    for base in seq:
        if base == 'G' or base == 'C':
            count+=1

    gc_percentage=count/len(seq)*100
    print("The GC content for the given seq is ", gc_percentage)


#2

def at_content(seq):
    count=0
    for base in seq:
        if base == 'A' or base == 'T':
            count+=1
    at_percentage=count/len(seq)*100
    print("The AT content for the given seq is ", at_percentage)



#3

def regional_gc_content(seq):
    initial=int(input("Give the start range for the region you would like to calculate GC content: "))
    final=int(input("Give the end range for the region you would like to calculate GC: "))
    count = 0
    for base in range(int(initial), int(final)+1):
        if seq[base] == "G" or seq[base] == "C":
            count+=1
        gc_percentage=count/len(seq)*100
    print("The GC content for a user defined region in  seq is ", gc_percentage)




#4

def gc_content(seq):
    count=0
def is_palindrome(seq):
    seq1=seq[::-1]
    if seq1 == seq:
        return True
    else:
        return False



#5
def nucleotide_dict(seq):

    base_A=0
    base_T=0
    base_G=0
    base_C=0
    base_N=0
    base_ambiguous=0
    for base in seq:
        if base =="A" :
            base_A=base_A+1
        elif base =="T" :
            base_T=base_T+1
        elif base =="G" :
            base_G=base_G+1
        elif base =="C" :
            base_C=base_C+1
        elif base =="N" :
            base_N=base_N+1
        else:
            base_ambiguous+=1

    nucleotide_count={"A":base_A,"T":base_T,"G":base_G,"C":base_C,"N":base_N,"ambiguous":base_ambiguous}
    print("The nucleotide count for the given seq is ", nucleotide_count)


#6
def count_percent_of_each_base(seq):
    count_A=0
    count_T=0
    count_G=0
    count_C=0
    count_N=0
    count_ambiguous=0
    for base in seq:
        if base == "A" :
            count_A+=1
        elif base == "T" :
            count_T+=1
        elif base == "G" :
            count_G+=1
        elif base == "C" :
            count_C+=1
        elif base == "N" :
            count_N+=1
        else:
            count_ambiguous+=1

    print("The percentage of A is ", count_A/len(seq)*100)
    print("The percentage of T is ", count_T/len(seq)*100)
    print("The percentage of G is ", count_G/len(seq)*100)
    print("The percentage of C is ", count_C/len(seq)*100)
    print("The percentage of N is ", count_N/len(seq)*100)
    print("The ambiguous base percent is ",count_ambiguous/len(seq)*100)

