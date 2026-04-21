import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('titanic')

fig, axes = plt.subplots(2, 1, figsize=(10, 10))
sns.scatterplot(data=df, x='age', y='fare', hue='survived', ax=axes[0])
axes[0].set_title('Scatter Plot - Age vs Fare')
sns.scatterplot(data=df, x='age', y='pclass', hue='sex', ax=axes[1])
axes[1].set_title('Scatter Plot - Age vs Pclass')
plt.tight_layout()
plt.show()

sns.violinplot(data=df, x='pclass', y='age', hue='sex', split=True)
plt.title("Violin Plot of Age by Passenger Class and Sex")
plt.xlabel("Passenger Class")
plt.ylabel("Age")
plt.show()

survival_data = df.groupby(['pclass', 'survived']).size().reset_index(name='count')
sns.lineplot(data=survival_data, x='pclass', y='count', hue='survived', marker='o')
plt.title("Passenger Survival Count by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.show()

sns.stripplot(data=df, x='sex', y='age', jitter=False, hue='survived', palette='Set2')
plt.title("Strip Plot of Age by Sex (No Jitter)")
plt.xlabel("Sex")
plt.ylabel("Age")
plt.legend(title="Survived", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

