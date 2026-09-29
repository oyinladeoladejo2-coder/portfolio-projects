# Implement contact_lookup(contact, key). 
# The contact argument is a dictionary. 
# Return the value for the given key. 
# If the key does not exist, return Not found.


def contact_lookup(contact, key):
    if key in contact:
        return contact[key]
    else:
        return "Not found"
