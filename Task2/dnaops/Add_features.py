"""
1. Find the first occurrence of a motif.
2. Find all positions of a given motif.
3. Return a k-mer breakdown (user inputs value of k).
4. Detect whether the DNA contains repeats (simple detection).
5. Identify longest continuous run of a single nucleotide.
"""

#1

def find_first_occurrence(seq):
    motif=input("Please enter the motif you would like to find the first occurrence: ")
    n=len(motif)
    for base in range(0,len(seq)-n):
        if seq[base:base+n] == motif:
            print("The first occurance of the motif is at ",base)
            print("The range of the motif is ", base,base+n)
            break



#2
def find_all_occurences(seq):
    motif = input("Please enter the motif you would like to find the first occurrence: ")
    n = len(motif)
    occurances=[]
    ranges=[]
    for base in range(0, len(seq) - n):
        if seq[base:base + n] == motif:
            i=base
            j=base,base+n
            occurances.append(i)
            ranges.append(j)
    print("The occurance of the motif are at indexes", occurances)
    print("The range of the motif are ", ranges)


#3
def k_mers(seq):
   k=int(input("Please enter the k value for which you would like to find the k-mers: "))
   kk_mers=[]
   for base in range(0, len(seq) -1):
      s=seq[base:base+k]
      kk_mers.append(s)

   print("The k-mer for the given seq are ", kk_mers)


#4
def check_repeats(seq):
    k = int(input("Please enter the k value for which you would like to find the k-mers: "))
    kk_mers = []
    count = 0
    repeat = False

    # Generate k-mers properly
    for base in range(0, len(seq) - k + 1):
        s = seq[base:base + k]
        kk_mers.append(s)

    # Compare k-mers for repeats
    for s in range(0, len(kk_mers) - 1):
        for t in range(s + 1, len(kk_mers)):
            if kk_mers[s] == kk_mers[t]:
                count += 1
                repeat = True

    print("The k-mers for the given seq are:", kk_mers)
    print("Is there any repeat?", repeat)
    print("The number of repeats is:", count)


#5

def longest_continous_run_of_base(seq):
    max_count = 1
    current_count = 1

    for i in range(len(seq) - 1):
        if seq[i] == seq[i + 1]:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 1

    # After the loop, check one last time:
    max_count = max(max_count, current_count)

    print(max_count)

