from sklearn import datasets, model_selection, tree, metrics, pipeline, feature_selection, ensemble

iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=.5, random_state=42)

clf = tree.DecisionTreeClassifier()

clf.fit(X_train, y_train)

predictions = clf.predict(X_test)

print(metrics.accuracy_score(y_test, predictions))

select = feature_selection.SelectKBest(k='all')
clf = ensemble.RandomForestClassifier()

steps = [('feature_selection', select), ('random_forest', clf)]

pipeline = pipeline.Pipeline(steps)

# pipeline.fit(X_train, y_train)
#
# y_pred = pipeline.predict(X_test)
#
# report = metrics.classification_report(y_test, y_pred)


parameters = {
    'feature_selection__k': [2, 4],
    'random_forest__n_estimators': [50, 100, 200],
    'random_forest__min_samples_split': [2, 3, 4, 5, 10]
}

cv = model_selection.GridSearchCV(pipeline, param_grid=parameters)

cv.fit(X_train, y_train)
y_pred = cv.predict(X_test)
report = metrics.classification_report(y_test, y_pred)

print(report)
