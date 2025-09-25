def strength(password):
    answer = []
    for i in range(len(password)):
        if len(password[i]) < 8 or password[i].isalpha():
           answer.append("weak")
        elif  len(password[i]) >= 12 and not password[i].isalnum() and not password[i].isspace():
            answer.append("strong")
        else:
            answer.append("ok")
    return answer
    
print(strength(["abc","School2025","L2arn!ngAI2025"]))
print(strength(["12345", "abcdefg"]))
print(strength(["helloworld", "PythonRocks"])) 
print(strength(["abc12345", "Password1", "Hello2025"]))
print(strength([""])) 
print(strength(["onlyletters", "Mix123", "GoodOne2023!", "Ultra$trongP@ssw0rd2025"]))
