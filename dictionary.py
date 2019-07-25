import json
# Declare dictionary
#user_name = {'Jolene': '14', 'Xun' : '48'}
#print(user_name['Jolene'])
#name = user_name ['Jolene']
# print(Joyce)

add = "Yes"

#create an empty dictionary
answers = {}

# create a list of survey questions
survey_questions = ["What is your name?", "How old are you?", "What is your favorite color?", "What is your favorite food?", "What is your favorite travel location?"]

# create a list of related keys

#question1 = ['Saira' : '', 'Gabby' : '', 'Meghan' : '']
#question2 = ['16' : '' : '17' : '']
keys = ["name","age", "color", "food", "travel"]

#word = keys['name']
#ord1 = keys[]

# loop through your list of survey questions and take user input for responses
#for key in users.items():
    #print(key_name) # key is stored in whatever you called  first variable
allUsers = []

while add == "Yes":
#create empty dictionary
    answers = {}
    index = 0
# loop through your list of survey questions and take user input for responses
    for questions in survey_questions: # loops through list
        response = input(questions)
        answers[keys[index]] = response
        index += 1 # index = index + 1
    add = input("Do you want to continue? Yes or No?")
#after all questions asked, add dictionary to the grand list
    allUsers.append(answers)


# print your dictionary
print(allUsers)

with open('dictionary.json') as f:
    try:
        olddata = json.load(f)
    except ValueError:
        olddata = []
allUsers.extend(olddata)
f.close()
f = open("dictionary.json", "w")
json.dump(allUsers, f)
f.close()
