from sklearn import datasets, model_selection, tree, metrics
from scipy.spatial.distance import euclidean as euc


class ScrappyKNN:
    def __init__(self):
        self.samples = None
        self.labels = None

    def fit(self, samples, labels):
        self.samples = samples
        self.labels = labels

    def predict(self, test_samples):
        return [self.closest(sample) for sample in test_samples]

    def closest(self, sample):
        return min([(euc(sample, s), l) for s, l in zip(self.samples, self.labels)], key=lambda a: a[0])[1]


iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=.5, random_state=42)

clf = ScrappyKNN()

clf.fit(X_train, y_train)

predictions = clf.predict(X_test)

print(metrics.accuracy_score(y_test, predictions))
