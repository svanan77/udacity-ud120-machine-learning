
def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)

    ### use the trained classifier to predict labels for the test features
    #### labels_test is what you are trying to predict
    pred = clf.predict(features_test)


    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    ###  X = features, Y = labels

    #Method 1
    from sklearn.metrics import accuracy_score
    #print accuracy_score(pred,labels_test)
    accuracy_m1 = accuracy_score(pred,labels_test)
    print "accuracy_m1=", accuracy_m1

    #Method 2 - Wrong as did not compare Y_predict with Y_actual
    #print clf.score(features_train, labels_train)
    ##accuracy_m2 = clf.score(features_train, labels_train)
    #accuracy_m2 = clf.score(pred,labels_test)
    ##print "accuracy_m2=", accuracy_m2

    #return accuracy_m1, accuracy_m2
    return accuracy_m1
