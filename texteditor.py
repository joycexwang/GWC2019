# Update this text to match your story.
start = '''
You finish school and wait for the school bus. Suddenly, a wizard appears.
He says: "I have kidnapped your family and brought them to Mars!You have three days to find them."
The wizard disappears, leaving a slip of paper: "Pick your ride: Rocket or Unicorn"
Two golden portals appear to your left and right.
'''

print(start)

print("Type 'Rocket' to go left or 'Unicorn' to go right.") # Update to match your story.
user_input = input()
if user_input == "Rocket" :
    print("You decide to go left and find yourself inside a rocket.")
    print("Hi! Welcome aboard. Good job, you chose the faster route. You'll arrive in a day.")
    print("Now in order to open the portal of the rocket when we arrive, you will need to find the key. Look behind the cupboard or look under the table.")
    print("Type 'Table' to go under or 'Cupboard' to go behind.")
    user_input = input()
    if user_input == "Table" :
        print("You decide to look under the table.")
        print("Sorry. The key is not here. Better luck next time.")
    elif user_input == "Cupboard" :
        print("You decide to look behind the cupboard")
        print("Good job, you found the key to leave the Rocket")
        print("We've arrived on Mars. Your family is locked up in a cell in the highest floor of the KnightMonkey Tower.")
        print("Do you want to go through the Fire Pit or through the Moonlight Lake?")
        print("Type 'Fire Pit' to go through or 'Moonlight Lake' to swim through.")
        user_input = input()
        if user_input == "Fire Pit" :
            print("You tred through the Fire Pit")
            print("Sorry. You are burned alive!!")
        elif user_input == "Moonlight Lake" :
            print("You swim through the Moonlight Lake")
            print("Congratulations! You've arrived at the KnightMonkey Tower!!")
            print("Take the elevator to the highest floor and you'll meet your family!")
elif user_input == "Unicorn" :
    print("You decide to go right and find yourself on a Unicorn.")
    print("Hello! Meet your new friend: Fluttershy.")
    print("Fluttershy is a little sleepy right now.")
    print("In order to get her to move faster, sing a song or dance.")
    print("Type 'Song' to sing or 'Dance' to dance")
    user_input = input()
    if user_input == "Song" :
        print("You decide to sing her the song: Rock-a-bye baby")
        print("Sorry. You made her fall asleep. Better luck next time.")
    elif user_input == "Dance" :
        print("You decide to dance to Party Rock Anthem")
        print("Good job, you energized her!")
        print("We've arrived on Mars. Your family is locked up in a cell in the highest floor of the KnightMonkey Tower.")
        print("Do you want to go through the Fire Pit or through the Moonlight Lake?")
        print("Type 'Fire Pit' to go through or 'Moonlight Lake' to swim through.")
        user_input = input()
        if user_input == "Fire Pit" :
            print("You tred through the Fire Pit")
            print("Sorry. You are burned alive!!")
        elif user_input == "Moonlight Lake" :
            print("You swim through the Moonlight Lake")
            print("Congratulations! You've arrived at the KnightMonkey Tower!!")
            print("Take the elevator to the highest floor and you'll meet your family!")
