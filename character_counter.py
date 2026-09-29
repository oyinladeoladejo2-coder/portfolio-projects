# Implement character_counter(text). 
# Return a dictionary where each character maps to how many times it appears. 
# Count spaces and symbols too. Do not use collections.Counter.


def character_counter(text):
    counts = {}

    for char in text:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] +=1
    return counts

