"""
Transformations
1. Generate the complement.
2. Generate the reverse.
3. Generate the reverse complement.
4. Convert the sequence to uppercase and standardize (ATGCN only).
5. Replace characters using mapping rules (example: A→T or G→C)
"""

#1
def complement(seq):
    complement = ""
    for base in seq:
        if base == 'A' :
            complement += 'T'
        elif base == 'T' :
            complement += 'A'
        elif base == 'G' :
            complement += 'C'
        elif base == 'C' :
            complement += 'G'
        else:
            complement += 'N'

    print("The complementary seq for the given seq is ", complement)




#2
def reverse_seq(seq):
  reversed_seq=seq[::-1]
  print("The reverse seq for the given seq is ", reversed_seq)



#3
def reverse_complement(seq):
    reverse_complement=""
    for base in seq:
        if base == 'A' :
            reverse_complement += 'T'
        elif base == 'T' :
            reverse_complement += 'A'
        elif base == 'G' :
            reverse_complement += 'C'
        elif base == 'C' :
            reverse_complement += 'G'
        else:
            reverse_complement += 'N'
    print("The reverse complement for the given seq is ", reverse_complement)


#4
def standerdize(seq):
    standerdized_seq=""
    for base in seq:
        if base == 'A' or base == 'T' or base == 'G' or base == 'C' or base == 'N':
            standerdized_seq += base
        elif base == " ":
            continue
        else:
            standerdized_seq += 'N'
    return standerdized_seq


#5

def convert_upper(seq):
    converted_seq=""
    for base in seq:
        converted_seq += base.upper()

    print("The converted seq for the given seq is ", converted_seq)



#6

def standerdize_and_convert_upper(seq):
    standerdized_seq=""
    for base in seq.upper():
        if base == 'A' or base == 'T' or base == 'G' or base == 'C' or base == 'N':
            standerdized_seq += base
        elif base == " ":
            continue
        else:
            standerdized_seq += 'N'


    print("The standerdized seq is", standerdized_seq)


#7
def map(seq):
    mapped_seq=""
    for base in seq:
      if base == 'A' :
          mapped_seq += 'T'
      elif base == 'T' :
          mapped_seq += 'A'
      elif base == 'G' :
          mapped_seq += 'C'
      elif base == 'C' :
          mapped_seq += 'G'
      elif base == 'N' :
          mapped_seq += 'N'
      else:
          mapped_seq += 'N'

    print("The mapped seq for the given seq is ", mapped_seq)

