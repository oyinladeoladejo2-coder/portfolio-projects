def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            return f"{word} is not a palindrome"
        

    return f"{word} is a palindrome"



word = input("Enter word:")
print (is_palindrome(word))
    
