
#features_train
X = [[0, 0], [2, 2]]
#labels_train
y = [0.5, 0.25]

from sklearn.tree import DecisionTreeRegressor
#Classifier and Fitting/Training
clf = DecisionTreeRegressor()
clf.fit(X, y)  

print(clf.predict([[1, 1]]))
print(clf.predict([[2., 2.]]))

## Output
## [ 0.5]
## [ 0.25]
