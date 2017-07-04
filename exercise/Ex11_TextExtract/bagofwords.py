#!/usr/bin/python

from sklearn.feature_extraction.text import CountVectorizer
#vectorizer = CountVectorizer()
vectorizer = CountVectorizer(stop_words="english")

String1= "hi Katie the self driving car will be late Best Sebastian"
String2= "Hi Sebastian the machine learning class will be great great great Best Katie"
String3= "Hi Katie the machine learning class will be most excellent"

email_list= [String1,String2,String3]

bag_of_words = vectorizer.fit(email_list)
#print "Fit", bag_of_words
bag_of_words = vectorizer.transform(email_list)
#print "Transform", bag_of_words
print "great", vectorizer.vocabulary_.get("great")
print "will", vectorizer.vocabulary_.get("will")
print "the", vectorizer.vocabulary_.get("the")
print "hi", vectorizer.vocabulary_.get("hi")
print "Katie", vectorizer.vocabulary_.get("Katie")
print "Sebastian", vectorizer.vocabulary_.get("Sebastian")
print "Best", vectorizer.vocabulary_.get("Best")
print "machine", vectorizer.vocabulary_.get("machine")


