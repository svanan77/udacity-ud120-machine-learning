#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()
################################################################################

### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

###################################################################
## Turn the comment off to enable test of the below classifiers  ##
###################################################################
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

#from sklearn.svm import SVC
#clf = SVC(kernel="linear", C=1.0) 
#clf = SVC(kernel="linear", C=10.0)
#clf = SVC(kernel="linear", C=100.0)
#clf = SVC(kernel="linear", C=1000.0)
#clf = SVC(kernel="linear", C=10000.0)
#clf = SVC(kernel="rbf", C=1.0) #Default
#clf = SVC(kernel="rbf", C=10.0)
#clf = SVC(kernel="rbf", C=100.0)
#clf = SVC(kernel="rbf", C=1000.0)
#clf = SVC(kernel="rbf", C=10000.0)
#clf = SVC(kernel="rbf", C=100000.0)   # --Winner--
#clf = SVC(kernel="rbf", C=1000000.0)  # --Winner--

#from sklearn.tree import DecisionTreeClassifier
#clf = DecisionTreeClassifier(criterion='gini', min_samples_split=2) #Default
#clf = DecisionTreeClassifier(criterion='gini', min_samples_split=10) 
#clf = DecisionTreeClassifier(criterion='gini', min_samples_split=20) 
#clf = DecisionTreeClassifier(criterion='gini', min_samples_split=25) 
#clf = DecisionTreeClassifier(criterion='gini', min_samples_split=30) 
#clf = DecisionTreeClassifier(criterion='gini', min_samples_split=40) 
#clf = DecisionTreeClassifier(criterion='gini', min_samples_split=50) 
#clf = DecisionTreeClassifier(criterion='entropy', min_samples_split=2)
#clf = DecisionTreeClassifier(criterion='entropy', min_samples_split=10)
#clf = DecisionTreeClassifier(criterion='entropy', min_samples_split=20)
#clf = DecisionTreeClassifier(criterion='entropy', min_samples_split=30)
#clf = DecisionTreeClassifier(criterion='entropy', min_samples_split=40)
#clf = DecisionTreeClassifier(criterion='entropy', min_samples_split=50)

#from sklearn.neighbors import KNeighborsClassifier
#clf = KNeighborsClassifier()

#from sklearn.ensemble import AdaBoostClassifier
#clf = AdaBoostClassifier()

#from sklearn.ensemble import RandomForestClassifier
#clf = RandomForestClassifier()

t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred=clf.predict(features_test)
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(pred,labels_test)
print "predicting time:", round(time()-t1, 3), "s"
print "accuracy:", accuracy

##########################
##  Output is as below  ##
##########################
#naive-bayes
#training time: 0.001 s
#predicting time: 0.005 s
#accuracy: 0.884
#
#SVM, Linear, C=1.0
#training time: 0.003 s
#predicting time: 0.001 s
#accuracy: 0.92
#
#SVM, Linear, C=10.0
#training time: 0.011 s
#predicting time: 0.002 s
#accuracy: 0.916
#
#SVM, Linear, C=100.0
#training time: 0.005 s
#predicting time: 0.001 s
#accuracy: 0.916
#
#SVM, Linear, C=1000.0
#training time: 0.021 s
#predicting time: 0.001 s
#accuracy: 0.92
#
#SVM, Linear, C=10000.0
#training time: 0.05 s
#predicting time: 0.001 s
#accuracy: 0.92
#
#SVM, RBF, C=1.0
#training time: 0.026 s
#predicting time: 0.005 s
#accuracy: 0.92
#
#SVM, RBF, C=10.0
#training time: 0.043 s
#predicting time: 0.004 s
#accuracy: 0.912
#
#SVM, RBF, C=100.0
#training time: 0.031 s
#predicting time: 0.003 s
#accuracy: 0.916
#
#SVM, RBF, C=1000.0
#training time: 0.026 s
#predicting time: 0.003 s
#accuracy: 0.924
#
#SVM, RBF, C=10000.0
#training time: 0.024 s
#predicting time: 0.003 s
#accuracy: 0.932
#
#SVM, RBF, C=100000.0
#training time: 0.11 s
#predicting time: 0.002 s
#accuracy: 0.944
#
#SVM, RBF, C=1000000.0
#training time: 1.52 s
#predicting time: 0.002 s
#accuracy: 0.948
#
#DT, Gini, min_samples_split=2
#training time: 0.001 s
#predicting time: 0.0 s
#accuracy: 0.908
#
#DT, Gini, min_samples_split=10
#training time: 0.006 s
#predicting time: 0.007 s
#accuracy: 0.912
#
#DT, Gini, min_samples_split=20
#training time: 0.001 s
#predicting time: 0.0 s
#accuracy: 0.924
#
#DT, Gini, min_samples_split=25
#training time: 0.001 s
#predicting time: 0.0 s
#accuracy: 0.916
#
#DT, Gini, min_samples_split=30
#training time: 0.001 s
#predicting time: 0.0 s
#accuracy: 0.916
#
#DT, Gini, min_samples_split=40
#training time: 0.001 s
#predicting time: 0.0 s
#accuracy: 0.912
#
#DT, Gini, min_samples_split=50
#training time: 0.001 s
#predicting time: 0.0 s
#accuracy: 0.912
#
#DT, Entropy, min_samples_split=2
#training time: 0.011 s
#predicting time: 0.001 s
#accuracy: 0.9
#
#DT, Entropy, min_samples_split=10
#training time: 0.012 s
#predicting time: 0.001 s
#accuracy: 0.912
#
#DT, Entropy, min_samples_split=20
#training time: 0.008 s
#predicting time: 0.001 s
#accuracy: 0.916
#
#DT, Entropy, min_samples_split=30
#training time: 0.007 s
#predicting time: 0.001 s
#accuracy: 0.916
#
#DT, Entropy, min_samples_split=40
#training time: 0.003 s
#predicting time: 0.0 s
#accuracy: 0.912
#
#DT, Entropy, min_samples_split=50
#training time: 0.003 s
#predicting time: 0.0 s
#accuracy: 0.912
#
#k-nearest neighbor
#training time: 0.001 s
#predicting time: 0.001 s
#accuracy: 0.92
#
#ada-boost
#training time: 0.093 s
#predicting time: 0.007 s
#accuracy: 0.924
#
#random forest
#training time: 0.048 s
#predicting time: 0.012 s
#accuracy: 0.916

try:
    #print "we are prettyPicture"
    prettyPicture(clf, features_test, labels_test)
except NameError:
    #print "we are passing"
    pass
