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

enron_data = pickle.load(open("/Users/angsherpa/ud120-projects/final_project/final_project_dataset.pkl", "r"))

#quiz 1
print(len(enron_data.keys()))

#print(enron_data.keys())
print(enron_data['METTS MARK'].keys())

#quiz 2
print(len(enron_data['METTS MARK'].keys()))

#quiz 3
count = 0
for user in enron_data:
    if enron_data[user]['poi'] == True:
        count += 1
print count

# quiz answer
print(enron_data['PRENTICE JAMES']['total_stock_value'])

#quiz answer
print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

#quiz answer
print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

#quiz answer
print(enron_data['SKILLING JEFFREY K']['total_payments'])
print(enron_data['LAY KENNETH L']['total_payments'])
print(enron_data['FASTOW ANDREW S']['total_payments'])

#quiz answer
count_salary = 0
count_email = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN':
        count_salary += 1
    if key in enron_data.keys():
        if enron_data[key]['email_address'] != 'NaN':
            count_email += 1
print(count_salary)
print(count_email)

#quiz answer
count_payment = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN':
        count_payment += 1
print(count_payment)

#quiz answer
poi_with_missing_payment = 0

for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True:
        poi_with_missing_payment += 1
print(poi_with_missing_payment)
