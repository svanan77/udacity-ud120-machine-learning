import numpy as np
#features_train
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
#labels_train
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB
#Classifier and Fitting/Training
clf = GaussianNB()
clf.fit(X, Y)

print(clf.predict([[-0.8, -1]]))
print(clf.predict([[30, 30]]))

## Output
## [1]
## [2]

#clf_pf = GaussianNB()
#clf_pf.partial_fit(X, Y, np.unique(Y))
#print(clf_pf.predict([[-0.8, -1]]))
