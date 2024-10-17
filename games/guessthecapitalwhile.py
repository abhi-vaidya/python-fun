import random

i = 1
attempt = 0
corectanswer = 0
wronganswer = 0
while i < 4:

  capitals = { "India" : "Delhi", "Poland" : "Warsaw", "UnitedKindgom": "London", "Germany": "Berlin" }

  question = str(random.choice(list(capitals.keys())))

  answer = str.capitalize(input(f"what is the capital of {question}?: "))

  if answer == capitals[question]:
     #print("Correct answer")
     corectanswer += 1
  else:
     #print("wrong Answer")
     wronganswer += 1    

  attempt -= 1
  i += 1

print(corectanswer)
print(wronganswer)