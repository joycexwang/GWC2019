#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
nameList = ["abby","sydney","jenn","cynthia","isabel","justine","veronica","lauren"]
appetizersList = ["ceaser salad","chicken noodle soup","tuna tartar"]
maincourseList = ["noodles","taco","pizza"]
dessertList = ["tiramisu","strawberry cake","sugar cookie"]
drinkList = ["strawberry banana smoothie","ice tea","bubble tea"]
#Generates a random integer.
aRandomIndex = randint(0, len(appetizersList)-1)
aRandomIndex1 = randint(0, len(maincourseList)-1)
print(appetizersList[aRandomIndex], maincourseList[aRandomIndex1])
