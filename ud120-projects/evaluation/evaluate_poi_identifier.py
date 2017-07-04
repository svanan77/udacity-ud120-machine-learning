#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
from time import time
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

#print "data_dict=", data_dict
### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = '../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)
#print "len(data)=", len(data)

### your code goes here 
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)

print "predicting time:", round(time()-t1, 3), "s"
print "accuracy:",accuracy

print "labels_test=", labels_test
print "pred=",pred
#print "len(pred)=",len(pred)
#print "sum(pred)=", sum(pred)

## Total people in Test Set = 29, len(features_test). 
## No of POI in the Test = 4.0, set sum(pred)
## Accuracy of Prediction if all predicted to be 0 is 0.862068965517

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

labels_test = true_labels
pred = predictions
true_positive=0.0
true_negative=0.0
false_positive=0.0
false_negative=0.0
precision=0.0
recall=0.0
for i in range(len(labels_test)):
  
  if (labels_test[i] == 1.0) and (labels_test[i] == pred[i]):
     true_positive+=1.0
  if (labels_test[i] == 0.0) and (labels_test[i] == pred[i]):
     true_negative+=1.0
  if (labels_test[i] == 0.0) and (labels_test[i] != pred[i]):
     false_positive+=1.0
  if (labels_test[i] == 1.0) and (labels_test[i] != pred[i]):
     false_negative+=1.0

precision=true_positive/(true_positive+false_positive)
recall=true_positive/(true_positive+false_negative)
print "true_positive=", true_positive, "true_negative=", true_negative, "false_positive=", false_positive,"false_negative=", false_negative, "precision=", precision, "recall=",recall
