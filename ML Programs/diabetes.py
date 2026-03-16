import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

data = pd.read_csv('diabetes.csv')
data.describe()
x = pd.DataFrame(data,columns=['Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])
y = data.Outcome.values.reshape(-1,1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state = 1)

clf = DecisionTreeClassifier(max_depth=3)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print(f"Accuracy : {accuracy_score(y_test,y_pred)*100:.2f}%")
feature_names = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
target_names = ['0','1']
fig = plt.figure(figsize=(23,20))
plot = tree.plot_tree(clf,feature_names=feature_names,class_names=target_names,filled=True)
plt.show()