text = "It's suggested to walk, study, and sleep everyday; for a great health."
result = []
word = ""

for char in text:
    if char != " ":
        if 'A' <=  char <= 'Z':
            word += chr(ord(char)+32)
        else:
            word += char
    elif( char == " " or char == "," or char == ";" or char == ":"):
        result.append(word)
        word = ""

if word:
    result.append(word)

print(result)
print(len(result))
