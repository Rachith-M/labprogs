from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

sample = load_iris()
X = sample.data
y = sample.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

classifier = GaussianNB()

classifier.fit(X_train,y_train)

prediction = classifier.predict(X_test)

accuracy = accuracy_score(y_test, prediction)
print(f"Accuracy is {accuracy*100:.2f}%")