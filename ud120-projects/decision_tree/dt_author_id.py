#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from class_vis import prettyPicture, output_image

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(min_samples_split=40)
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)

#print "len(features_test)=", len(features_test)
#print "len(features_test[0])=", len(features_test[0])
#print "len(labels_test)=", len(labels_test)
#print "len(labels_test[0])=", len(labels_test[0])
#print "labels_test=",labels_test

print "predicting time:", round(time()-t1, 3), "s"
print "accuracy:",accuracy

#prettyPicture(clf, features_test, labels_test)
#plt.show()
#output_image("test.png", "png", open("test.png", "rb").read())
#########################################################

#print "len(features_train[0])=", len(features_train[0])
#selector = SelectPercentile(f_classif, percentile=10)
#len(features_train[0])= 3785
#training time: 41.603 s
#predicting time: 0.047 s
#accuracy: 0.9795221843

#selector = SelectPercentile(f_classif, percentile=1)
#len(features_train[0])= 379
#training time: 4.147 s
#predicting time: 0.004 s
#accuracy: 0.967007963595
