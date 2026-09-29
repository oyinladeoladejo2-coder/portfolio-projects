# Implement group_by_first_letter(names). 
# Return a dictionary where each key is the uppercase first letter of a name and each value is a list of names that start with that letter.
#  Ignore empty names after stripping spaces. Preserve the order of names inside each group.

def group_by_first_letter(names):
    result = {}
    for name in names:
        clean_name= name.strip()
        if clean_name:
            key = clean_name[0].upper()
            result.setdefault(key, []).append(clean_name)    
    return result

