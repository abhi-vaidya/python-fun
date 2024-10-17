import random

number = random.randint(4, 20)

userchoice = int(input("Guess the number: "))
if userchoice == number:
    print ("Bingo, You guessed correct")
elif userchoice >  number:
    print ("Too high")
elif  userchoice <  number:
    print ("Too Low")  


print (f"computer choice was {number}")