def age_category(age, country):
        if age >= 18 and country.strip().lower() == "nigeria":
               return "Eligible"
        else:
              return "Not eligible"
        
