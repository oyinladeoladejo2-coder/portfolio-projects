def second_largest(num):
    largest = float('-inf')
    second = float('-inf')
    for number in num:
        if number > largest:
            second = largest
            largest = number
        elif number  > second and number != largest:
            second = number 

    return second


numbers = ([4, 9, 2, 9, 7])

second =(second_largest(numbers))

print("second:", second)
            
    

        


        
        

