import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv('planets.csv')
sns.set_palette("husl")
plt.figure(figsize=(12, 6))
scatter = sns.scatterplot(
    data=df,
    x='year',
    y='distance',
    hue='method',
    size='mass',
    sizes=(20, 200),
    alpha=0.7
)
plt.title("Distance vs Year Method and Mass")
plt.xlabel("Discovery Year")
plt.ylabel("Distance")
plt.legend(bbox_to_anchor=(1.05,1), loc='upper left', borderaxespad=0)
plt.tight_layout()
plt.show()
 
method_distance = df.groupby('method')['distance'].mean().reset_index()
plt.figure(figsize=(12, 6))
bar = sns.barplot(
    data=method_distance,
    x='method',
    y='distance',
    palette='viridis'
)
plt.title("Average Distance by Discover Method")
plt.xlabel("Discovery Method")
plt.ylabel("Average Distance")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()