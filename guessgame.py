import random

# A list of words that
potential_words = ["tiger", "phonebooth", "smile", "sagittarius", "psyco"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
length = len(word)
current_word = ["_"] * length # TIP: the number of letters should match the word
print(current_word)
# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")
	iter = 0
	for l in word:
		if l == guess:
			current_word[iter] = guess
		iter += 1
	print(current_word)
	if guess not in word:
		print("sorry, that's not in the word")
		fails = fails+1
		print("You have " + str(maxfails - fails) + " tries left!")
	if ("_") not in current_word:
		print("win")
		break
else:
	print("try again")
