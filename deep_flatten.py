# Implement deep_flatten(items). 
# Return a flat list containing every non-list value from items, no matter how deeply nested the lists are. 
# Students may need to research recursion. 
# Preserve the left-to-right order.


def deep_flatten(items):
    flatten = []
    for item in items:
        if isinstance(item, list):
            flatten.extend(deep_flatten(item))
        else:
            flatten.append(item)
    return flatten
