# Given a paragraph of text, count how many times each word appears and store it in a dictionary. Then, find and print the single most frequent word. 
# Examples
# Input: "Python is fun, and Python is powerful!"
# Output: Most frequent word: python (2) 
# Constraints
# Treat uppercase and lowercase as the same.
# You must strip basic punctuation (like commas and periods) manually without using the re module or string.punctuation.
# After counting, you must find the most frequent word without using max() or sorting the dictionary.
# Do not use collections.Counter


def word_frequency(text):
    oyin ={}
  
    split_sentence = text.split()

   #  word_count = 0

    for _, word  in enumerate(split_sentence):
         word = word.lower().replace(",", "").replace("!", "").replace(".", "").replace("?", "")
    
         if word in oyin:
            oyin[word] += 1

         else:
            oyin[word] = 1

    split_sentence=[]
    print(oyin)

        
sample_texts = "do you know oyinlade? because oyinlade is smart, and she is going to be advanced on ai/ml and become sucessfull.."
word_frequency(sample_texts)

