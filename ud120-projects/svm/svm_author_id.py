#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
# C (10.0, 100., 1000., and 10000.). 

from sklearn.svm import SVC
#clf = SVC(kernel="linear")
#clf = SVC(kernel="linear", C=10.0)
#clf = SVC(kernel="linear", C=100.0)
#clf = SVC(kernel="linear", C=1000.0)
#clf = SVC(kernel="linear", C=10000.0)

#clf = SVC(kernel="rbf")
#clf = SVC(kernel="rbf", C=10.0)
#clf = SVC(kernel="rbf", C=100.0)
#clf = SVC(kernel="rbf", C=1000.0)
clf = SVC(kernel="rbf", C=10000.0)

# The below 2 lines slices the training dataset down to 1% of its original size, 
# tossing out 99% of the training data. 

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred=clf.predict(features_test)
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(pred,labels_test)

print "predicting time:", round(time()-t1, 3), "s"
print "accuracy:", accuracy

print "len(pred)=", len(pred)
print "len(labels_test)=", len(labels_test)

print "pred=",pred
print "labels_test=",labels_test

christ=0
#print "Christ=",christ
for i in range(len(pred)):
 if pred[i]==1:
    christ+=1

print "Christ=",christ

#print "Element:10=",pred[10]
#print "Element:26=",pred[26]
#print "Element:50=",pred[50]
#Element:10= 1
#Element:26= 0
#Element:50= 1

##### 100% training set, C=1  #####
##Output - Linear
#no. of Chris training emails: 7936
#no. of Sara training emails: 7884
#training time: 148.004 s
#predicting time: 16.147 s
#accuracy: 0.984072810011

##Output - RBF
#training time: 935.726 s
#predicting time: 103.447 s
#accuracy: 0.492036405006

##### 100% training set, C=10000  #####
##Output - Linear
#training time: 76.852 s
#predicting time: 7.139 s
#accuracy: 0.994880546075

##Output - RBF
#training time: 109.631 s
#predicting time: 10.14 s
#accuracy: 0.990898748578

##### 1% training set, C=1 #####
##Output - Linear
#training time: 0.119 s
#predicting time: 1.012 s
#accuracy: 0.884527872582

##Output - RBF
#training time: 0.164 s
#predicting time: 1.213 s
#accuracy: 0.616040955631

##### 1% training set, C=10 #####
##Output - Linear
#training time: 0.12 s
#predicting time: 0.903 s
#accuracy: 0.874857792947

##Output - RBF
#training time: 0.13 s
#predicting time: 1.183 s
#accuracy: 0.616040955631

##### 1% training set, C=100 #####
##Output - Linear
#training time: 0.121 s
#predicting time: 0.806 s
#accuracy: 0.8606370876

##Output - RBF
#training time: 0.13 s
#predicting time: 1.179 s
#accuracy: 0.616040955631

##### 1% training set, C=1000 #####
##Output - Linear
#training time: 0.116 s
#predicting time: 0.819 s
#accuracy: 0.8606370876

##Output - RBF
#training time: 0.125 s
#predicting time: 1.101 s
#accuracy: 0.821387940842

##### 1% training set, C=10000 #####
##Output - Linear
#training time: 0.118 s
#predicting time: 0.814 s
#accuracy: 0.8606370876

##Output - RBF
#training time: 0.122 s
#predicting time: 0.95 s
#accuracy: 0.892491467577

#########################################################


