from sklearn import tree, svm, neighbors

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'female', 'male', 'male', 'female', 'female', 'male', 'male']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
clf_svm = svm.SVC()
clf_svm = clf_svm.fit(X, Y)
clf_knn = neighbors.KNeighborsClassifier()
clf_knn = clf_knn.fit(X, Y)

data = [[170, 70, 39]]

prediction1 = clf.predict(data)
prediction2 = clf_svm.predict(data)
prediction3 = clf_knn.predict(data)

if prediction1[0] == 'male':
    print('Gender: male (Tree)')
else:    print('Gender: female (Tree)')

if prediction2[0] == 'male':
    print('Gender: male (SVM)')
else:    print('Gender: female (SVM)')

if prediction3[0] == 'male':
    print('Gender: male (KNN)')
else:    print('Gender: female (KNN)')