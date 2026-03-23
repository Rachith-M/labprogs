import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train_scaled,y_train)
y_pred_train = clf.predict(X_train_scaled)
predictions = clf.predict(X_test)

correct_predictions = 0
wrong_predictions = 0

for i in range(len(predictions)):
    if(predictions[i] == y_test[i]):
        print(f"correct prediction: predicted class {predictions[i]},actual class{y_test[i]}")
        correct_predictions+=1
    else:
        print(f"wrong prediction: predicted class {predictions[i]},actual class{y_test[i]}")
        wrong_predictions+=1
        
print(f"Accuracy : {accuracy_score(y_train,y_pred_train)*100:.2f}%")
print(f"Wrong predictions : {wrong_predictions}")
print(f"Correct predictions : {correct_predictions}")
