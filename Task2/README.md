"""
Task 2 - Build a Python DNA Utility Library: dnaops

Purpose:
dnaops is Python package that provides basic tools for working
with DNA sequences.It helps users check,clean,transform and analyze 
DNA using simple functions.

Installation instructions:
git clone https://github.com/IBAB-BioHackTeam/Savitha_Elumalai.git
cd Savitha_Elumalai
from dnaops import Basic_seq_check.py
from dnaops import Sequence_Analysis.py
from dnaops  import Transformations.py
from dnaops import Add_features.py
from dnaops import Bonus.py



List of implemented functions:

A.Sequence Functions (Basic_seq_check.py)

1.length(seq)
2.count_bases(seq)
3.validate_DNA(seq)
4.replace_ambiguous_bases(seq)
5.no_of_purines(seq)
6.no_of_pyrimidines(seq)

B.Transformations (Transformations.py)

7.complement(seq)
8.reverse_seq(seq)
9.reverse_complement(seq)
10.standerdize(seq)
11.convert_upper(seq)
12.standerdize_and_convert_upper(seq)
13.map(seq)

C.Analysis Functions ( Sequence_Analysis.py)

14.gc_content(seq)
15.at_content(seq)
16.regional_gc_content(seq)
17.is_palindrome(seq)
18.nucleotide_dict(seq)
19.count_percent_of_each_base(seq)

D.Additional Features (Add_features.py)

20.find_first_occurrence(seq)
21.find_all_occurences(seq)
22.k_mers(seq)
23.check_repeats(seq)
24.longest_continous_run_of_base(seq)

E.Some more Functions (Bonus.py)

25.longest_GC_region(seq)
26.longest_alternating(seq)
27.count_transitions(seq)
 



Author : Savitha Elumalai
Date: 11th Dec 2025