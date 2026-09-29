# Implement clean_words(words). 
# Return a new list where each word is stripped of surrounding spaces and converted to lowercase. 
# Ignore words that become empty after stripping. 
# Use a list comprehension.


def clean_words(words):
    words = [word.strip().lower() for word in words if word.strip()]
    return words
