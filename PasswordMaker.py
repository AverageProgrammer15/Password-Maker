import random
AlphabetsCapitalized = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
AlphabetsNonCapital = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
SpecialChars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "\"", ",", ".", "<", ">", "/", "?", "\\", "|", "`", "~"]
NumberTable = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

ChooseLimit = 1

UseSpecialChar = input("Use special characters? (True or False)")

if UseSpecialChar == "True":
    ChooseLimit = ChooseLimit + 1

UseNumbers = input("Use numbers? (True or False)")

if UseNumbers == "True":
    ChooseLimit = ChooseLimit + 1

NumofChars = input("How long do you want your password to be(Numbers)")

NumofChars = int(NumofChars)





Password = []
Choose = None
for x in range(NumofChars):
   Choose = random.randint(0,ChooseLimit)
   if Choose == 0:
       Password.append(AlphabetsCapitalized[random.randint(0,25)])
   elif Choose == 1:
        Password.append(AlphabetsNonCapital[random.randint(0,25)])
   elif Choose == 2:
        Password.append(SpecialChars[random.randint(0,31)])
   
   elif Choose == 3: 
       Password.append(NumberTable[random.randint(0,9)])  

   


print(''.join(Password))
