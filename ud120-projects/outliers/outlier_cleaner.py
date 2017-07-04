#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for i in xrange(0,len(ages)):
      cleaned_data.append((ages[i][0],net_worths[i][0],pow((net_worths[i][0]-predictions[i][0]),2)))
      #cleaned_data_sorted = sorted(cleaned_data, key=lambda tup: tup[2])
      #cleaned_data = sorted(cleaned_data, key=lambda tup: tup[2],reverse=True)
      cleaned_data = sorted(cleaned_data, key=lambda tup: tup[2])
    #print "cleaned_data=",cleaned_data
    a10percent=int(0.1*len(ages))
    for i in xrange(0,a10percent):
      del cleaned_data[len(ages)-1-i]
    #print "cleaned_data_sorted=",cleaned_data_sorted
    #print "cleaned_data=",cleaned_data
    return cleaned_data

