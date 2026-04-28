import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = sns.load_dataset('titanic')  # Or use pd.read_csv('titanic.csv')
# Reorder 'class' axis based on survival rate
order = df.groupby('class')['survived'].mean().sort_values().index

sns.catplot(data=df, x='class', y='survived', kind='bar', order=order)
plt.title("Survival Rate by Class (Reordered)")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.show()
#violin
sns.violinplot(data=df, x='class', y='age', hue='sex', split=True)
plt.title("Violin Plot of Age by Class and Sex")
plt.xlabel("Passenger Class")
plt.ylabel("Age")
plt.show()
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.lineplot(data=df, x='class', y='age', estimator='mean', ax=axes[0])
axes[0].set_title("Avg Age by Class")


sns.lineplot(data=df, x='class', y='fare', estimator='mean', ax=axes[1])
axes[1].set_title("Avg Fare by Class")


survival_rate = df.groupby('class')['survived'].mean().reset_index()
sns.lineplot(data=survival_rate, x='class', y='survived', marker='o', ax=axes[2])
axes[2].set_title("Survival Rate by Class")

plt.tight_layout()
plt.show()

sns.set_palette("husl")

sns.scatterplot(data=df, x='age', y='fare', hue='sex', style='survived')
plt.title("Scatter Plot of Age vs Fare (Colored by Sex & Style by Survival)")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.legend(title='Sex / Survival', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
