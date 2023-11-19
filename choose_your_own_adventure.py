name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input ("You are on a muddy road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across? Type walk to walk around or swim to swim across: ").lower()
     
    if answer == "swim":
        print("You swam across and was eaten by a crocodile!")   
    elif answer == "walk":
        print("You walked for so long that you ran out of water and lost the game!")
    else: 
        print("Not a valid option. You loose.")

elif answer == "right":
    answer = input("You come to an old wobbly bridge. Do you want to cross it or go back (cross/back)? ").lower()
    if answer == "back":
        print("You go back to the cave and get eaten by the ogre! You loose!")   
    elif answer == "cross":
        answer == input ("You cross the bridge and see a smoky hut and a lad is outside. Do you talk to him (yes/no)? ").lower()
        if answer == "yes":
            print("You talk to him and he gives you a pendant. You win!")
        elif answer == "no":
            print("You ignore the lad and get lost. You loose!")
        else:
            print("Not a valid option. You loose!")

    else: 
        print("Not a valid option. You loose.")
else:
    print("Not a valid option. You lose.")

print("Thankyou for trying", name)

