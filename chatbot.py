# --- Define your functions below! ---
import random

def intro():
    print("Hi! Welcome to Joyce's chatbot.")

def process_input(answer):
    if is_valid_input(answer):
        greeting()
    else:
        default()

def is_valid_input(word):
    validList = ["hi", "hello", "hey", "what's up", "sup"]
    if word in validList:
        return True
    else:
        return False

def greeting():
    name = input("What is your name?")
    process_name(name)

def default():
    print("very cool")
    name = input("What is your name?")
    process_name(name)

def process_name(name):
    print("Hi " + name)

def joke():
    answer1 = input("Do you want to hear a joke?")
    if is_valid_input1(answer1) == True:
        say_joke(answer1)
    else:
        print("Do you want to play a game?")
        if is_valid_input1(answer1) == True:
            say_game()

def say_joke(answer1):
    aRandomIndex = randint(0, len(jokeList)-1)
    jokeList = ["why don't you write with a broken pencil?", "what do you call a train carrying bubblegum", "How many times can you subtract 10 from 10?"]
    print(jokeList(aRandomIndex))

def is_valid_input1(answer1):
    validList1 = ["yes","sure","okay","fine"]
    if answer1 in validList1:
        return True
    else:
        return False

# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        process_input(answer)
        joke()












# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
