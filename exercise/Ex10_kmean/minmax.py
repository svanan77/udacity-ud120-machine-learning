#!/usr/bin/python

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

import numpy
data = numpy.array([[115.0], [140.0], [175.0]])
data_rescaled = scaler.fit_transform(data)

print "data=",data
print "data_rescaled=",data_rescaled
