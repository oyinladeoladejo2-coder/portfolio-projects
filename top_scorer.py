# Implement top_scorer(scores). 
# The scores argument is a dictionary mapping student names to numeric scores. 
# Return the name of the student with the highest score. 
# If the dictionary is empty, return No scores. 
# If there is a tie, return the name that comes first alphabetically.

def top_scorer(scores):
    if not scores:
        return  'No scores'
    best_student = min(scores, key=lambda name: (-scores[name], name))
    return best_student
