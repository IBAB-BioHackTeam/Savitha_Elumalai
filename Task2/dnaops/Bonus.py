"""
1.Longest GC rich region
2. Longest alternating patterns
3.Count consecutive base transitions
"""
#1
def longest_GC_region(seq):
    max_len = 0
    current = 0

    for base in seq:
        if base == 'G' or base == 'C':
            current += 1
        else:
            if current > max_len:
                max_len = current
            current = 0

    if current > max_len:   # handle end of string
        max_len = current

    return max_len

#2
def longest_alternating(seq):
    if len(seq) == 0:
        return 0

    max_len = 1
    current = 1

    for i in range(len(seq)-1):
        if seq[i] != seq[i+1]:
            current += 1
        else:
            if current > max_len:
                max_len = current
            current = 1

    if current > max_len:
        max_len = current

    return max_len


#3
def count_transitions(seq):
    transitions = 0

    for i in range(len(seq)-1):
        if seq[i] != seq[i+1]:
            transitions += 1

    return transitions
