#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("C:\\code\\udacity_ml_project\\final_project\\final_project_dataset.pkl", "r"))

# print enron_data.keys()

count = 0
for person in enron_data:
    if enron_data[person]["poi"] == True:
        if enron_data[person]["total_payments"] == 'NaN':
            count += 1
print count

# print enron_data["PRENTICE JAMES"]["total_stock_value"]

#print enron_data["COLWELL WESLEY"]

# print enron_data["SKILLING JEFFREY K"]["total_payments"]
# print enron_data["LAY KENNETH L"]["total_payments"]
# print enron_data["FASTOW ANDREW S"]["total_payments"]

# print enron_data["SKILLING JEFFREY K"]
# print enron_data["LAY KENNETH L"]["total_payments"]
# print enron_data["FASTOW ANDREW S"]["total_payments"]

# count = 0
# for person in enron_data:
#     if enron_data[person]["total_payments"] == 'NaN':
#         count += 1
# print count

# print 31./156.