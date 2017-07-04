#!/usr/bin/python

""" lecture and example code for decision tree unit """

import sys
from time import time
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
#from classifyDT import classify

features_train, labels_train, features_test, labels_test = makeTerrainData()



### the classify() function in classifyDT is where the magic
### happens--fill in this function in the file 'classifyDT.py'!
#clf = classify(features_train, labels_train)

#from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
#Classifier and Fitting/Training
clf = DecisionTreeClassifier()
#clf = DecisionTreeClassifier(min_samples_split=2)
#clf = DecisionTreeClassifier(min_samples_split=50)
t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print "predicting time:", round(time()-t1, 3), "s"

print "accuracy:",accuracy

#min_samples_split=1 default
#training time: 0.001 s
#predicting time: 0.0 s
#accuracy: 0.908

#min_samples_split=2
#training time: 0.001 s
#predicting time: 0.0 s
#accuracy: 0.908

#min_samples_split=50
#training time: 0.001 s
#predicting time: 0.0 s
#accuracy: 0.912


#### grader code, do not modify below this line
#Disable output image when computing accuracy

prettyPicture(clf, features_test, labels_test)
#output_image("test.png", "png", open("test.png", "rb").read())

