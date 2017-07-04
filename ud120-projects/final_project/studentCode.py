import pickle
from get_data import getData

def computeFraction( poi_messages, all_messages ):
    """ given a number messages to/from POI (numerator) 
        and number of all messages to/from a person (denominator),
        return the fraction of messages to/from that person
        that are from/to a POI
   """


    ### you fill in this code, so that it returns either
    ###     the fraction of all messages to this person that come from POIs
    ###     or
    ###     the fraction of all messages from this person that are sent to POIs
    ### the same code can be used to compute either quantity

    ### beware of "NaN" when there is no known email address (and so
    ### no filled email features), and integer division!
    ### in case of poi_messages or all_messages having "NaN" value, return 0.
    fraction = 0.

    if ((poi_messages!='NaN') and (all_messages!='NaN')):
       fraction = float(poi_messages)/float(all_messages)
    #print "poi_messages=",poi_messages,"all_messages=",all_messages, "fraction=",fraction

    return fraction


data_dict = getData() 

submit_dict = {}

plot_dict = {}
plot_dict["fraction_from_poi"] = []
plot_dict["to_messages"] = []
plot_dict["from_poi_to_this_person"] = []
plot_dict["fraction_to_poi"] = []
plot_dict["from_messages"] = []
plot_dict["from_this_person_to_poi"] = []

for name in data_dict:

    data_point = data_dict[name]
    #print
    from_poi_to_this_person = data_point["from_poi_to_this_person"]
    to_messages = data_point["to_messages"]
    fraction_from_poi = computeFraction( from_poi_to_this_person, to_messages )
    #print fraction_from_poi
    data_point["fraction_from_poi"] = fraction_from_poi
    plot_dict["fraction_from_poi"].append(fraction_from_poi)    
    plot_dict["to_messages"].append(to_messages)
    plot_dict["from_poi_to_this_person"].append(from_poi_to_this_person)

    from_this_person_to_poi = data_point["from_this_person_to_poi"]
    from_messages = data_point["from_messages"]
    fraction_to_poi = computeFraction( from_this_person_to_poi, from_messages )
    #print fraction_to_poi
    submit_dict[name]={"from_poi_to_this_person":fraction_from_poi,
                       "from_this_person_to_poi":fraction_to_poi}
    data_point["fraction_to_poi"] = fraction_to_poi
    plot_dict["fraction_to_poi"].append(fraction_to_poi)
    plot_dict["from_messages"].append(from_messages)
    plot_dict["from_this_person_to_poi"].append(from_this_person_to_poi)

#print "submit_dict=",submit_dict 
#print "data_point=",data_point
#print "plot_dict=",plot_dict

#import matplotlib.pyplot as plt
#plt.clf()
#plt.scatter(plot_dict["fraction_from_poi"], plot_dict["fraction_to_poi"], color="b", label="POI")
#plt.scatter(ages_test, net_worths_test, color="r", label="test data")
#plt.plot(ages_test, reg.predict(ages_test), color="black")
#plt.legend(loc=2)
#plt.xlabel("from_poi_to_this_person")
#plt.ylabel("from_this_person_to_poi")
#plt.show()
#####################

def submitDict():
    return submit_dict

