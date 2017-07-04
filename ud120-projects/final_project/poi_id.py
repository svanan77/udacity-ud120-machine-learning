#!/usr/bin/python

import os
import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
import matplotlib.pyplot
from studentCode import computeFraction
from time import time

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary','bonus','total_stock_value'] # You will need to use more features

def main():
### Load the dictionary containing the dataset
 with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

 poi_counter=0
 non_poi_counter=0
 NaN_counter={}
 NaN20_counter={}
 for name in data_dict:
  NaN20_counter=0
  for feature in data_dict[name]:
    if ((feature!='poi') and (data_dict[name][feature]=="NaN")):
      NaN20_counter+=1

    if feature in features_list:
      if feature not in NaN_counter:
        NaN_counter[feature]=0

      if (feature=='poi'):
         if (data_dict[name][feature]):
           poi_counter+=1
         else:
           non_poi_counter+=1
      else:
        if (data_dict[name][feature]=='NaN'):
           NaN_counter[feature]+=1

 '''
 # The below is for Understanding the Dataset

 print "total number of data points=",len(data_dict)
 print "POI=",poi_counter,",non-POI=",non_poi_counter
 print "No of features used=", len(features_list)
 for feature in NaN_counter.keys():
  print "feature=",feature, ",missing values=",NaN_counter[feature]
 '''
### Task 2: Remove outliers
 del data_dict['TOTAL']                           #Non person
 del data_dict['THE TRAVEL AGENCY IN THE PARK']   #Non person
 del data_dict['LOCKHART EUGENE E']               #All features NaN

 #'''
### Task 3: Create new feature(s)
 features_list.append('fraction_from_poi')
 features_list.append('fraction_to_poi')
 for name in data_dict:
    from_poi_to_this_person = data_dict[name]["from_poi_to_this_person"]
    to_messages = data_dict[name]["to_messages"]
    fraction_from_poi = computeFraction( from_poi_to_this_person, to_messages )
    data_dict[name]["fraction_from_poi"] = fraction_from_poi
    #print "fraction_from_poi=", fraction_from_poi

    from_this_person_to_poi = data_dict[name]["from_this_person_to_poi"]
    from_messages = data_dict[name]["from_messages"]
    fraction_to_poi = computeFraction( from_this_person_to_poi, from_messages )
    data_dict[name]["fraction_to_poi"] = fraction_to_poi
    #print "fraction_to_poi", fraction_to_poi
 #'''

### Store to my_dataset for easy export below.
 my_dataset = data_dict

### Extract features and labels from dataset for local testing
 data = featureFormat(my_dataset, features_list, sort_keys = True)

 '''
 # The below is for feature rescaling
 from sklearn.preprocessing import MinMaxScaler
 scaler = MinMaxScaler()
 data = scaler.fit_transform(data)
 '''

 '''
 # The below is for plotting

 for point in data:
    salary = point[1]
    bonus = point[2]
    total_stock = point[3]
    from_poi = point[4]
    to_poi = point[5]
    #matplotlib.pyplot.scatter( from_poi, to_poi )
    #matplotlib.pyplot.scatter( salary, bonus )
    #matplotlib.pyplot.scatter( salary, total_stock )
    matplotlib.pyplot.scatter( total_stock, to_poi )

 #matplotlib.pyplot.xlabel("from_poi")
 #matplotlib.pyplot.ylabel("to_poi") 

 #matplotlib.pyplot.xlabel("salary")
 #matplotlib.pyplot.ylabel("bonus")

 #matplotlib.pyplot.xlabel("salary")
 #matplotlib.pyplot.ylabel("total_stock")

 matplotlib.pyplot.xlabel("total_stock")
 matplotlib.pyplot.ylabel("to_poi")

 matplotlib.pyplot.show()
 '''

 labels, features = targetFeatureSplit(data)
 #print "labels=",labels
 #print "features=", features

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.

 options=[1,2,3,4,5,6]
 #options=[2]
 for opt in options:
  if (opt==1):
    from sklearn.naive_bayes import GaussianNB
    print "#GaussianNB()"
    clf = GaussianNB()
    Task_5(clf,features,labels,my_dataset,features_list)
    Task_6(clf,my_dataset,features_list)
  elif (opt==2):
    clist=['gini','entropy']
    mlist=[2,10,20,25,30,40,50]
    from sklearn.ensemble import RandomForestClassifier
    for citem in clist:
       for mitem in mlist:
          print "#RandomForestClassifier(criterion='"+citem+"', min_samples_split="+str(mitem)+")" 
          clf = eval("RandomForestClassifier(criterion='"+citem+"', min_samples_split="+str(mitem)+")")          
          Task_5(clf,features,labels,my_dataset,features_list)
          Task_6(clf,my_dataset,features_list)
  elif (opt==3):
    clist=['gini','entropy']
    mlist=[2,10,20,25,30,40,50]
    from sklearn.tree import DecisionTreeClassifier
    for citem in clist:
       for mitem in mlist:
          print "#DecisionTreeClassifier(criterion='"+citem+"', min_samples_split="+str(mitem)+")" 
          clf = eval("DecisionTreeClassifier(criterion='"+citem+"', min_samples_split="+str(mitem)+")")
          Task_5(clf,features,labels,my_dataset,features_list)
          Task_6(clf,my_dataset,features_list)
  elif (opt==4):
    wlist=['uniform','distance']
    alist=['auto','brute','ball_tree','kd_tree']
    nlist=[2,3,4,5,6,7,8]    
    from sklearn.neighbors import KNeighborsClassifier
    for witem in wlist:
       for aitem in alist:
          for nitem in nlist:
             print "#KNeighborsClassifier(n_neighbors="+str(nitem)+", algorithm='"+aitem+"', weights ='"+witem+"')" 
             clf = eval("KNeighborsClassifier(n_neighbors="+str(nitem)+", algorithm='"+aitem+"', weights ='"+witem+"')")
             Task_5(clf,features,labels,my_dataset,features_list)
             Task_6(clf,my_dataset,features_list)
  elif (opt==5): 
    alist=['SAMME.R','SAMME']
    llist=[0.80,0.85,0.90,0.95,1.0]
    nlist=[20,30,40,50,60,70,80]
    from sklearn.ensemble import AdaBoostClassifier
    for aitem in alist:
       for litem in llist:
          for nitem in nlist:
             print "#AdaBoostClassifier(n_estimators="+str(nitem)+", algorithm='"+aitem+"', learning_rate="+str(litem)+")" 
             clf = eval("AdaBoostClassifier(n_estimators="+str(nitem)+", algorithm='"+aitem+"', learning_rate="+str(litem)+")")
             Task_5(clf,features,labels,my_dataset,features_list)
             Task_6(clf,my_dataset,features_list)
  elif (opt==6): 
    klist=['linear','rbf','poly','sigmoid']
    #clist=[1.0,10.0,100.0,1000.0,10000.0]
    clist=[1.0,10.0,100.0,1000.0,10000.0,100000.0,1000000.0]
    from sklearn.svm import SVC
    for citem in clist:
       for kitem in klist:
          print "#SVC(kernel='"+kitem+"', C="+str(citem)+")"
          clf = eval("SVC(kernel='"+kitem+"', C="+str(citem)+")")
          Task_5(clf,features,labels,my_dataset,features_list)
          Task_6(clf,my_dataset,features_list)

def Task_5(clf,features,labels,my_dataset,features_list):
### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
  from sklearn.cross_validation import train_test_split
  features_train, features_test, labels_train, labels_test = \
      train_test_split(features, labels, test_size=0.3, random_state=42)

  t0 = time()
  clf.fit(features_train,labels_train)
  #print ""
  print "training time:", round(time()-t0, 3), "s"

  t1 = time()
  pred=clf.predict(features_test)
  from sklearn.metrics import accuracy_score
  accuracy=accuracy_score(pred,labels_test)
  print "predicting time:", round(time()-t1, 3), "s"
  print "accuracy:", format(accuracy, '.4f')
  print ""

  '''
  print "Features List=", features_list
  print "Features Importance=", clf.feature_importances_

  from sklearn.feature_selection import SelectPercentile, f_classif
  selector = SelectPercentile(f_classif, percentile=10)
  selector.fit(features_train, labels_train)
  print "Features List=", features_list
  print "Selector Scores SelectPercentile=", selector.scores_
  '''
  '''
  from sklearn.feature_selection import SelectKBest, f_classif
  selector1 = SelectKBest(f_classif, k=2)
  selector1.fit(features_train, labels_train)
  print "Features List=", features_list
  print "Selector Scores SelectKBest=", selector1.scores_
  '''
  '''
  from sklearn.feature_selection import RFE
  selector2 = RFE(clf, 2, step=1)
  selector2.fit(features_train, labels_train)
  print "Features List=", features_list
  print "Selector Scores RFE=", selector2.n_features_
  print "Selector Scores RFE=", selector2.support_ 
  print "Selector Scores RFE=", selector2.ranking_ 
  '''


  labels_test = labels_test
  pred = pred

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

  #print "true_positive=", format(true_positive, '.4f')
  #print "true_negative=", format(true_negative, '.4f')
  #print "false_positive=", format(false_positive, '.4f')
  #print "false_negative=", format(false_negative, '.4f')

  if (true_positive+false_positive==0):
     precision=0.0000
  else:
     precision=true_positive/(true_positive+false_positive)

  if (true_positive+false_negative==0):
     recall=0.0000
  else:
     recall=true_positive/(true_positive+false_negative)

  #print "Target precision and recall >0.3000"
  #print "precision=", format(precision, '.4f')
  #print "recall=",format(recall, '.4f')
  #print ""
  return

def Task_6(clf, my_dataset, features_list):
### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

  dump_classifier_and_data(clf, my_dataset, features_list)
  t3 = time()
  os.system('python tester.py')
  print "executing tester.py time:", round(time()-t3, 3), "s"
  print ""
  print "###########################################################################################################################"
  print ""
  return

if __name__ == '__main__':
    main()
