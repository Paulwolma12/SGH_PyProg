# Please write a program that reads a text file containing some text and for each word in the file counts how many times "it" appears.
# Please note you can use a dictionary structure. Before starting to count words it might be necessary to delete
# all punctuation and special symbols (new line, tab etc.) and put all words in lower case.


# To do this task I used Chapter 5 from The Lion of Petra novel I had in text format

#Reading the file from the directory
f = open("Lion_of_Petra.txt", "r")

data = f.read()

f.close()

# print(data)

# Changing the text to lower case
text = data.lower()

# Creating a list of punctuation we will remove from the text
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# looping through each element to look for punctuation listed above and replace it with ""
for el in text:
    if el in punc:
        text = text.replace(el, "")

#Creatign a function for the word counter
def wordcounter(x):
    counts = dict() # Creating dict of word counts
    words = x.split() # splitting the words in to list of words

# Loop through each word and recognising if the word is new or adds one if it is a match to a previous word
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

word_counted = wordcounter(text) # entering the text into the function and defining it

#sorting the words from most used words to least
word_sorted = {key: word_counted[key] for key in sorted(word_counted, key=word_counted.get, reverse=True)}
print(word_sorted)
