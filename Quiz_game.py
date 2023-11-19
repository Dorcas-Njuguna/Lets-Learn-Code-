print("Welcome to my computer quiz!")

playing = input("Do you want to play with me? ")

if playing.lower() != "yes":
    quit()

print("okay! Let's play:)")
score = 0

answer = input("What does IDE stand for? ")
if answer.lower() == "integrated development environment":
    print("Correct!")
    score += 1  # Also as score = score + 1. I.e. take values of score and add 1.
else : 
    print("Incorrect!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else : 
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else : 
    print("Incorrect!")

answer = input("What is the best yoghurt flavour? ")
if answer.lower() == "apricot":
    print("Correct!")
    score += 1
else : 
    print("Incorrect!")

print ("You got " + str(score) + " questions correct!" )
print ("You got " + str((score/4) *100) + "%." )