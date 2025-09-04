text = "Anan and Benjawan want to play badminton before dinner"
list_word = []
word = ""
#loop ตัวอักษรใน txt
for char in text:
    if char != " ":
        if 'A' <= char <= 'Z':
           word += chr(ord(char)+32)
        else:
            word += char
    else:
        list_word.append(word)
        word = ""

# keep last word into list_word 
if word:
    list_word.append(word)

print(list_word)
print(len(list_word))
