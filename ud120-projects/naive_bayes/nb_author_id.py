#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred,labels_test)
print "predicting time:", round(time()-t1, 3), "s"

print "accuracy:", accuracy

#no. of Chris training emails: 7936
#no. of Sara training emails: 7884
#training time: 1.093 s
#predicting time: 0.181 s
#accuracy: 0.973265073948

#########################################################




