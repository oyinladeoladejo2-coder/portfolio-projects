# Implement point_summary(point). 
# The point argument is a tuple containing x and y.
# Return a dictionary with keys named x, y, and manhattan. 
# The manhattan value is the absolute value of x plus the absolute value of y.

def point_summary(point):
    (x, y) = point
    points = {
        "x" : x,
        "y": y,
        "manhattan": abs(x) + abs(y) 
    }
    return points
