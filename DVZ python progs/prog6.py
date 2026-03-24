import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('planets.csv')
plt.figure(figsize=(10,6))
sns.scatterplot(
    data=data,
    x='year',
    y='distance',
    hue='mass',
    #style='mass',
    size='mass',
    sizes=(20,200),
    palette='viridis',
    alpha=0.7
)

plt.title('Distance covered year wise with Mass as additional features')
plt.xlabel('Year')
plt.ylabel('Distance')
plt.legend(title="Mass Category", bbox_to_anchor=(1.05,1), loc='best')
plt.grid(True)
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(
    data=data,
    x='orbital_period',
    bins=20,
    kde=True,
    color='skyblue'    
)

plt.title("Distribution of orbital periods")
plt.xlabel("Orbital Period")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()