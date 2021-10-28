import random

#random password generator function, takes in a parameter (int), the length of the password
def randPassword(x: int):
    randPasswordList = []
    #add the first capitalized letter
    randUpperChar = chr(random.randint(65,90))
    randPasswordList.append(randUpperChar)

    #generate lower characters
    tempList = []
    for i in range(x-3):
        randLowerChar = chr(random.randint(97,122))
        tempList.append(randLowerChar)

    #add lower chars to password
    random.shuffle(tempList)
    randPasswordList.extend(tempList)

    #add random number and symbol at the end
    randPasswordList.append(chr(random.randint(48,57)))
    randPasswordList.append(chr(random.randint(33,47)))
    
    pwd = "".join(randPasswordList)
    return pwd

print("Your generated password is: "+ randPassword(8))