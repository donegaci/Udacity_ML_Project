
import os
import pickle
import re
import sys

sys.path.insert(0, "C:\\code\\udacity_ml_project\\tools")
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""

from_sara  = open("C:\\code\\udacity_ml_project\\text_learning\\from_sara.txt", "r")
from_chris = open("C:\\code\\udacity_ml_project\\text_learning\\from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        # temp_counter += 1
        # if temp_counter < 200:
            path = os.path.join('C:\\code\\udacity_ml_project', path[:-1])
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            stemmed_text = parseOutText(email)
            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            words_to_remove = ["sara", "shackleton", "chris", "germani", "sshacklensf", "cgermannsf"]
            for word in words_to_remove:
                stemmed_text = stemmed_text.replace(word, " ")
            ### append the text to word_data
            word_data.append(stemmed_text)
            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            if name == "sara":
                from_data.append(0)
            elif name == "chris":   
                from_data.append(1)

            email.close()

        


print "emails processed"
from_sara.close()
from_chris.close()

#print from_data
# print word_data[152]

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )

### in Part 4, do TfIdf vectorization here

from sklearn.feature_extraction.text import TfidfVectorizer
vect = TfidfVectorizer(stop_words = "english")
vect.fit_transform(word_data)

print len(vect.get_feature_names())