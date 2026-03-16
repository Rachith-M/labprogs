import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer


sample = pd.read_csv("spam.csv")
X = sample.v2
y = sample.v1

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

classifier = MultinomialNB()

classifier.fit(X_train,y_train)

prediction = classifier.predict(X_test)

accuracy = accuracy_score(y_test, prediction)
print(f"Accuracy is {accuracy*100:.2f}%")