Design Choice:
The package is divided into five modules, each focusing on a 
logically distinct category of DNA operations.

Package Structure

Package name: dnaops

modules:

Basic_seq_check.py
Transformations.py
Sequence_Analysis.py
Add_features.py
Bonus.py
__init__.py

Contains simple loops.

Inputs: 
1.string DNA sequence
2.uppercase preferred
3.Invalid characters allowed only for cleaning functions.

outputs:
Mostly return values or print statements of results.

Error handling:
Invalid bases are converted to N
Assumes string input.


Possible limitations:
1.No FASTA file parsing
2.Limited error handling
3.No optimization for large sequences.
