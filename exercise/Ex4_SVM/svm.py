
#features_train
X = [[0, 0], [1, 1]]
#labels_train
y = [0, 1]

from sklearn.svm import SVC
#Classifier and Fitting/Training
## Options --- 
##    SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
##    decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
##    max_iter=-1, probability=False, random_state=None, shrinking=True,
##    tol=0.001, verbose=False)

clf = SVC()
clf.fit(X, y)  

print(clf.predict([[2., 2.]]))

## Output
## [1]


