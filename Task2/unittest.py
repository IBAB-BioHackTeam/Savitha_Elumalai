from dnaops import Add_features
from dnaops import Basic_seq_check
from dnaops import Bonus
from dnaops import Sequence_Analysis
from dnaops import Transformations

seq = "ATGCTTTAGCGANTTGCAXTGCTNRYGCTA"

print("These are some of tests based on each of the modules in the dnaops package.")

print(Add_features.k_mers(seq))
print(Basic_seq_check.no_of_purines(seq))
print(Bonus.count_transitions(seq))
print(Sequence_Analysis.nucleotide_dict(seq))
print(Transformations.standerdize_and_convert_upper(seq))
