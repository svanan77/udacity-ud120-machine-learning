#!/usr/bin/python

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

#vectorizer = CountVectorizer()
vectorizer = CountVectorizer(stop_words="english")

#vectorizer = TfidfVectorizer()
#vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')

sw = stopwords.words("english")
#sw = set(stopwords.words("english"))

#print "len(sw)=", len(sw)
#print "sw=", sw

stemmer = SnowballStemmer("english")
#print stemmer.stem("responsiveness")
#print stemmer.stem("responsivity")
#print stemmer.stem("unresponsive")
#print stemmer.stem("response")
#print stemmer.stem("responsitivity")
#print stemmer.stem("respond")


String1= "hi Katie the self driving car will be late Best Sebastian"
String2= "Hi Sebastian the machine learning class will be great great great Best Katie"
String3= "Hi Katie the machine learning class will be most excellent"

email_list= [String1,String2,String3]
email_list_sw = []
email_list_st = []

for string in email_list:
   string_sw =""
   words = string.split()
   for word in words:
      if word not in sw:
         string_sw = str(string_sw+" "+word)
   email_list_sw.append(string_sw)

for string in email_list_sw:
   string_st =""
   words = string.split()
   for word in words:
      word_st=stemmer.stem(word)
      string_st = str(string_st+" "+word_st)
   email_list_st.append(string_st)

print "email_list=",email_list
print "email_list_sw=",email_list_sw
print "email_list_st=",email_list_st

bag_of_words = vectorizer.fit(email_list_st)
#print "Fit", bag_of_words
bag_of_words = vectorizer.transform(email_list_st)
print "Transform=", bag_of_words
#print "great", vectorizer.vocabulary_.get("great")
#print "will", vectorizer.vocabulary_.get("will")
#print "the", vectorizer.vocabulary_.get("the")
#print "hi", vectorizer.vocabulary_.get("hi")
#print "Katie", vectorizer.vocabulary_.get("Katie")
#print "Sebastian", vectorizer.vocabulary_.get("Sebastian")
#print "Best", vectorizer.vocabulary_.get("Best")
#print "machine", vectorizer.vocabulary_.get("machine")

#selector = SelectPercentile(f_classif, percentile=10)
#selector.fit(bag_of_words)
#bag_of_words = selector.transform(bag_of_words).toarray()
#print "Selector=", bag_of_words
