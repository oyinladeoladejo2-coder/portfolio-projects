# Implement collect_until_stop(items). 
# Loop through the list and collect items until an item becomes stop after stripping spaces and converting to lowercase. 
# Return the collected items before stop. 
# Use break when stop is found.


def collect_until_stop(items):
    item7 = []
    for item in items:
        if item.strip().lower() == 'stop':
            break
        else:
            item7.append(item)
        
    return item7
