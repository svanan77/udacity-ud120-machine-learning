#!/usr/bin/python

""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    Xmin = min(arr)
    Xmax = max(arr)
    data_prime = []
    for X in arr:
      Xprime = float(X - Xmin)/float(Xmax - Xmin)
      data_prime.append(Xprime)
      print "X=",X,"Xprime=", Xprime
    return data_prime

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)
