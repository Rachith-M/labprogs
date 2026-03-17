import matplotlib.pyplot as plt
import numpy as np

languages = ['Fict', 'Tech', 'Moti', 'Business', 'Nutri', 'Dev']
sales = [5.2,19.6, 8.7, 8, 7.7, 3.7]
colors = ['blue','green','red','purple','orange','cyan']
plt.figure(figsize = (8,6))
plt.barh(languages, sales, color = colors)
plt.xlabel('Sales (in million)')
plt.ylabel('Book Categories')
plt.title("Book Title by Category")
plt.xticks(np.arange(0, 25, 5))
plt.yticks(languages)
plt.legend(["Book Sales"],loc = 'upper right')
plt.tight_layout()
plt.savefig('book_sales_horizontal_bar.png')
plt.show()

categories = ['A', 'B', 'C', 'D', 'E']
means_men = np.array([22, 30, 35, 35, 26])
means_women = np.array([25, 32, 30, 35, 29])
bar_width = 0.5
plt.bar(categories, means_men, bar_width, label="Men", color='skyblue')
plt.bar(categories, means_women, bar_width, bottom=means_men, label="Women", color='pink')
plt.xlabel("Categories")
plt.ylabel("Scores")
plt.title("Scores by Group and Gender")
plt.xticks(categories)
plt.yticks(np.arange(0, 81, 10))

for i in range(len(categories)):
    for i in range(len(categories)):
        plt.text(i, means_men[i] / 2, str(means_men[i]), ha='center', color='black', fontsize=10)
        plt.text(i, means_men[i] + means_women[i] / 2, str(means_women[i]), ha='center', color='black', fontsize=10)
plt.legend(loc ='upper right')
plt.tight_layout()
plt.savefig('stacked_bar_plot.png')
plt.show()