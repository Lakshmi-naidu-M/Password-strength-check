password = input('Enter your password: \n').strip()
print(f"Your password is {password}")

specialCharacter = [] 


numerics = []


alphabetsChars = []

for i in range(len(password)):
    if(not password[i].isalnum()):
        specialCharacter.append(password[i])
    if(password[i].isnumeric()):
        numerics.append(password[i])

    if(password[i].isalnum() and ( not password[i].isnumeric())):
        alphabetsChars.append(password[i])
    
    
if(len(password)<8):
    print('Your password should be atleast 8 charaacters')
    

elif((len(specialCharacter) != 0) and (len(numerics) != 0) and (len(alphabetsChars)!=0)):
    print('Your password is strong')


elif((len(specialCharacter) == 0) and (len(numerics) != 0) and (len(alphabetsChars)!=0)):
    print('Your password is good')

elif((len(specialCharacter) == 0) and (len(numerics) == 0) and (len(alphabetsChars)!=0)):
    print('Your password is weak')