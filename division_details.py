def division_details(a, b):

    division = {
        "true_division": round(a/b, 2),
        "floor_division": a // b,
        "remainder": a % b
    }

    return division
