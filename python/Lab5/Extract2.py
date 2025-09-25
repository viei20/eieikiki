def extract_words(text):

    text_split = text.split()
    word = [i for i in text_split if len(i)>= 4]
    return word

print( extract_words("Don't judge a book by its cover."))
print( extract_words("All that glitters is not gold."))
print( extract_words("The multinational corporation's decentralization strategy required  comprehensive reorganization of their compartmentalized departmentalization systems across intercontinental subsidiaries."))