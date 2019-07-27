'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''
#part1
import json
from textblob import TextBlob
#part2
import matplotlib.pyplot as plt
import numpy as np
#part3
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
polarity = []
subjectivity = []
#filteredWords[word] = count
bigtweet = ""
for tweet in tweetData:
    text = tweet["text"]
    tb = TextBlob(text)
    #tb.polarity
    polarity.append(tb.polarity)
    #tb.subjectvity
    subjectivity.append(tb.subjectivity)
#part 3
    bigtweet += text

tb1 = TextBlob(bigtweet)
filterd = {}
allfrequencies = []
wordsList = tb1.words

for word in wordsList:
    badwords = ["and", "then", "but", "what", "when", "where"]
    if len(word) < 5:
        continue
    if word in badwords:
        continue
    if not word.isalpha():
        continue
    else:
        filterd[word] = tb1.word_counts[word]

print(filterd)
allfrequencies.append(filterd)

with open('words.json') as f:
    try:
        olddata = json.load(f)
    except ValueError:
        olddata = []
allfrequencies.extend(olddata)
f.close()
f = open("words.json", "w")
json.dump(allfrequencies, f)
f.close()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()


    #if tweetstring.isalpha():
        #wordCount = tb1.word_count()
        #print(wordCount)
    #else:
        #break

average = sum(polarity)/len(polarity)
#print(average)

average1 = sum(subjectivity)/len(subjectivity)
#print(average1)

# Textblob sample:
#tb = TextBlob("You are a brilliant computer scientist.")
#print(tb.polarity)

#histogram
plt.xlabel('Polarity')
plt.ylabel('Amount of Tweets')
plt.title('Polarity of Tweets')
plt.axis([-1, 1, 0, 60])
plt.grid(True)
plt.hist(polarity, bins = [-1.1, -0.75, -0.5, -0.25, 0, 0.25, 0.50, 0.75, 1.1])
#plt.show()

plt.xlabel('Subjectivity')
plt.ylabel('Amount of Tweets')
plt.title('Subjectivity of Tweets')
plt.axis([0, 1, 0, 60])
plt.grid(True)
plt.hist(subjectivity, bins = [0, 0.25, 0.50, 0.75, 1.1])
#plt.show()
