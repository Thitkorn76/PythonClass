import random

print('what is my magic nunber  (1 to 100) ?')
mynumber = random.randint(1,100)
ntries = 1
yourguess = -1

while ntries < 7 and yourguess != mynumber :
    msg = str(ntries) + '>>'
    if (ntries == 6) :
            print('No time to find number ')
    
    yourguess = int(input(msg))
    
    if yourguess > mynumber:
            print("--> Too High")
    
    if yourguess < mynumber: 
            print("--> Too low")
    ntries +=1

if yourguess == mynumber :
       print(" Yse! it's ", mynumber)
else :
       print("Sorry! my number is", mynumber)
