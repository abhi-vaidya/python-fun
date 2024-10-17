#Maximum 4 players
#Roll the dice producing numbers between 1 to 6
#each player has his turn to roll out dice
#Add the total for each player based on the number produced by each dice roll out 
#If player reach on ladder, add bonus total
#If player reach on snakes head, cut the points from total
#Any player reaches to number 100,  Game ends with Player win.
#press q to quit game

import random

def rolldice():
   return random.randint(1, 6)
    
def playsnakesandladders():
   playernames = {}
   for p in ["player1", "player2", "player3", "player4"]: 
      player = str.capitalize(input(f"{p}, Enter your name: "))
      if player != "":
        playernames[player] = 0

   #return print(playernames)
   total = 0  
   while True:
      snakestable = {27 : 6, 35 : 5, 39 :  3, 50 : 34, 59 : 46, 66 : 24, 73 : 12, 76 : 63, 97 : 86, 99 : 26 }
      laddertable = {2 : 23, 7 : 29, 22 : 41, 30 : 32, 44 : 58, 28 : 77, 54 : 69, 70 : 90, 80 : 83, 87 : 93 }
      for players in list(playernames.keys()):
         ans = input(f"ready to roll dice {players},Press y to continue: ")
         if ans == "y":
            num = rolldice()
            if num == 6:
                print(f"{players} got number 6 and got double roll dice")
                num = num + rolldice()
            total = playernames[players] + int(num)
            playernames[players] = total
            for sn in list(snakestable.keys()):
                if playernames[players] == sn:
                    playernames[players] = snakestable[sn]
                    print(f"Oops, you got Snake and you are down to {snakestable[sn]}")
                    print('''
                                 * * * *
                              *          *     *********      **********        *********      *********
                           ***     *       *****         ********        **********       ********          **********_____________  
                           ***             *****         ********        **********       ********          ********** 
                              *        *       *********      **********        *********      ********* 
                                 * * * * 
                         ''')
            for ld in list(laddertable.keys()):
                if  playernames[players] == ld:
                    playernames[players] = laddertable[ld]
                    print(f"Congratulations, you got ladders and you are at {laddertable[ld]}")
                    print('''
                                 ||__||
                                 ||__||
                                 ||__||
                                 ||__||
                                 ||__||
                                 ||__||
                                 ||__||
                                 ||__||
                                 ||__||
                                 ||__||
                                 ||__||
                                 ||  || 
                                 
                           ''')       
            print(f"{players}, your number is ... {num} and your total is {playernames[players]}" )
            if playernames[players] >= 100:
               break
         else:
            if ans == "q":
               break
            else:
              print("Only y key is accepted, you lost a chance.")    
            
            
      if playernames[players] >= 100:
              print(f"{players} is won!")
              break
      if ans == "q":
         print("Exiting game")
         break            
      
#Play Game                       
playsnakesandladders()