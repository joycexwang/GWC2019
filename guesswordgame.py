import random
iter = 0
# A list of words that
potential_words = ["tiger", "phone", "smile", "virgo", "psyco"]

word = random.choice(potential_words)

# Use to test your code:
print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = ["_", "_", "_", "_", "_"] # TIP: the number of letters should match the word
print(current_word)
print(input("Guess a letter: "))

# Some useful variables\
correct = word
guess = []
maxfails = 7
fails = 0
out_of_guesses = False

while fails < maxfails:
	guess = input("Guess a letter: ")
	fails += 1


print("you win!")

	for guess in word:
		print "Sorry"

for let in word:
	if let == guess:


	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")
