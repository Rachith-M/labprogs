import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

sns.displot(data=df, x='age', kde=False, bins = 30, color = 'skyblue')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

sns.kdeplot(data=df, x ='age',fill = True, color = 'purple')
plt.title("Age distribution with KDE")
plt.xlabel("Age")
plt.ylabel("Density")
plt.show()

avg_fare = df.groupby('pclass')['fare'].mean().reset_index()
sns.lineplot(data = avg_fare, x='pclass', y='fare', marker='o', color ='red')
plt.title("Average fare by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")
plt.show()

sns.scatterplot(data=df, x='age', y='fare', hue='pclass', palette='viridis')
plt.title('Age vs Fare by Passenger Class')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()