import random

name = "Anthony"
question = "Am I the coolest"
answer = ""
random_number = random.randint(1,12)

#print(random_number)

if random_number == 1:
  answer = "Sure whatever."
elif random_number == 2:
  answer = "Who asks this kind of question?"
elif random_number == 3:
  answer = "Darn tootin'"
elif random_number == 4:
  answer = "Your question cannot be answered at this time. Please hang up and try again."
elif random_number == 5:
  answer = "Better believe it pal."
elif random_number == 6:
  answer = "Fuggetaboutit."
elif random_number == 7:
  answer = "Bury your hopes on that one."
elif random_number == 8:
  answer = "Negative."
elif random_number == 9:
  answer = "In this economy?"
elif random_number == 10:
  answer = "Yeah."
elif random_number == 11:
  answer = "I do not understand the statement."
elif random_number == 12:
  answer = "I guess."
else:
  answer = "Error"

if name == "":
  print("Question: " + question)
else:
  print(name + " asks, " + question)

if question == "":
  print("Error: Please enter a question")
else:
  print("Magic 8-Ball's answer: " + answer)
