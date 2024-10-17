import random
import os

'''
Valid options:
Rock
Paper
Scissor
'''
i = 1

win = 0
lose = 0

while (i < 4):
   computerchoice = random.choice(["Rock", "Paper", "Scissor"])
   userchoice = str.capitalize(input("enter your choice: "))

   if ((userchoice != "Rock") and (userchoice != "Paper") and (userchoice != "Scissor")):
         print("Invalid Choice. Choose from Rock, Paper, Scissor")
         break

   if (userchoice == computerchoice):
         print("Same Choices")
         exit
   else:
      if ((userchoice == "Paper" and computerchoice == "Rock") or (userchoice == "Rock" and computerchoice == "Scissor") or (userchoice == "Scissor" and computerchoice == "Paper")):
            print(f"You win!")
            win += 1
      else: 
         print("Computer have won!")
         lose += 1   
        
   i += 1        
    
if ( win == lose ):
       
   print ( '''
      *************
      *************
      *************
      *************
      ITs A Tie!!!                    
   ''')

else:
   if ( win > lose ):
      print ( '''
      *************
      *************
      *************
      *************
      Yay!You win!!!                    
   ''')
   else:
      print ( '''
      *************
      *************
      *************
      *************
      Better luck next time!!!!                    
   ''')      
