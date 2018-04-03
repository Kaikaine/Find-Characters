def find_characters (words, char):
    
    new_words = []

    for i in words:
        if char in i:
            new_words.append(i)
    print new_words
    return new_words

find_characters (['hello','world','my','name','is','Anna'], "o")
