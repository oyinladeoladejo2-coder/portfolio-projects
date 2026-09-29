# Implement unique_tags(tags). 
# Clean each tag by stripping spaces and converting to lowercase.
# Ignore empty tags.
# Return a sorted list of unique cleaned tags.

def unique_tags(tags):
    new_tags = []
    for tag in tags:
        clean_tag = tag.strip().lower()
        if clean_tag:
            if clean_tag not in new_tags:
                new_tags.append(clean_tag)
    return sorted(new_tags) 
