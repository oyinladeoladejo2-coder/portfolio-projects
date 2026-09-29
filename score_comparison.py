# Implement set_comparison(a, b). 
# Return a dictionary with keys named both, only_a, and only_b.
#  The both value should be a sorted list of items in both lists.
#  The only_a value should be a sorted list of items only in a. 
#  The only_b value should be a sorted list of items only in b.

def set_comparison(a, b):
    both = sorted(set(a) & set (b))
    only_a = sorted(set(a) - set(b))
    only_b = sorted(set(b)- set(a))

    oyin = {
        "both": both,
        "only_a": only_a,
        "only_b": only_b
    }
    return oyin

