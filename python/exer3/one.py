text = input()
list_word = []
word = ""
for char in text:
    if char != " ":

        word += char
    else:
        list_word.append(word)
        word = ""

if word:
    list_word.append(word)


first_letter = []
for word in list_word:
    word = word.strip()
    if len(word) > 0:
        first_letter.append(word[0])
    else:
        first_letter.append('')

upper_word =[]
for word in first_letter:
    upper_word.append(word.upper())

i = 0
while i < len(upper_word):
    print(f"{upper_word[i]}.")
    i += 1



 

