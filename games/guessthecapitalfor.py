
correctanswer = 0
wronganswer = 0
result = ""
capitals = { "India" : "Delhi", "Poland" : "Warsaw", "UnitedKindgom": "London", "Germany": "Berlin" }

for key in capitals:

  answer = str.capitalize(input(f"what is the capital of {key}?: "))

  if answer == capitals[key]:
     #print("Correct answer")
     correctanswer += 1
  else:
     #print("wrong Answer")
     wronganswer += 1    


if correctanswer > (len(capitals) - 2):
   result = "You win"
else:
   result = "You lost"

print(f"You have answered {correctanswer} correct answers")
print(f"You have answered {wronganswer} wrong answers")
print(f"Overall result is: {result}")