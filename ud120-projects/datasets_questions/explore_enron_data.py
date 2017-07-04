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

counter = 0
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
for name in enron_data.keys():
  if (enron_data[name]["poi"] == 1):
     #counter += 1
     pass

  temp= enron_data[name]['salary']
  try:
   val = int(temp)
   #counter +=1
  except ValueError:
   pass

  if (enron_data[name]['email_address'] != 'NaN'):
    #counter += 1
    pass

  if (enron_data[name]['total_payments'] == 'NaN'):
    #counter += 1
    pass

  if ((enron_data[name]["poi"] == 1) and (enron_data[name]['total_payments'] == 'NaN')):
    counter += 1
    pass

  tokens = name.split()
  if (len(tokens)==2):
    lname = tokens[0]
    fname = tokens[1]
    if (fname=='JAMES' and lname =='PRENTICE'):
      #print "James Prentice's total value of stock is $", enron_data[name]['total_stock_value']
      pass

    if (fname=='WESLEY' and lname =='COLWELL'):
      #print "The number of Email messages from Wesley Colwell to persons of interest is", enron_data[name]['from_this_person_to_poi']
      pass
    if (lname=='LAY' or lname=='SKILLING' or lname=='FASTOW'):
       #print name,enron_data[name]['total_payments']
       pass

  if (len(tokens)==3):
    lname = tokens[0]
    fname = tokens[1]
    mname = tokens[2]
    if (fname=='JEFFREY' and mname== 'K' and lname =='SKILLING'):
      #print "Jeffrey K Skilling's total exercised stock options is $", enron_data[name]['exercised_stock_options']
      pass
    if (lname=='LAY' or lname=='SKILLING' or lname=='FASTOW'):
       #print name,enron_data[name]['total_payments']
       pass
#

print counter
print len(enron_data)
print float(counter+10)/float(len(enron_data)+10)

#counter = 0
for line in file("../final_project/poi_names.txt"):
  tokens = line.split()
  if (len(tokens)>1):
    #counter += 1
    dir_ = tokens[0]           
    fname_ = tokens[2]
    lname_ = tokens[1]                    
    #print "dir_:",dir_, ",name_:",fname_,lname_[:-1]
#print counter

